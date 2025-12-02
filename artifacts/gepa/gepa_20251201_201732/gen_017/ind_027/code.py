
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes: kick=36, snare=38, hihat=42
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=80, pitch=drum_kick, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=80, pitch=drum_snare, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=60, pitch=drum_hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line with roots and fifths, chromatic approaches
# Time signatures: 4/4, 160 BPM, each bar is 1.5 seconds
# Each beat is 0.375 seconds

# Bass Line: D - F - A - B (root, b7, 5, 6) in the key of D minor
# Bar 2: D - F - A - B
# Bar 3: A - B - D - F
# Bar 4: F - A - B - D

bass_notes = [
    # Bar 2
    (1.5, 2, 0.125),  # D2
    (1.75, 2, 0.125), # F2
    (2.0, 2, 0.125),  # A2
    (2.25, 2, 0.125), # B2
    
    # Bar 3
    (2.5, 2, 0.125),  # A2
    (2.75, 2, 0.125), # B2
    (3.0, 2, 0.125),  # D2
    (3.25, 2, 0.125), # F2
    
    # Bar 4
    (3.5, 2, 0.125),  # F2
    (3.75, 2, 0.125), # A2
    (4.0, 2, 0.125),  # B2
    (4.25, 2, 0.125), # D2
]

for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar (Dm7, G7, Cm7, F7)
# Comp on 2 and 4

# Define chord voicings (root, 3, 7, 9)
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
# Bar 5: F7 (F, A, C, Eb)

# Bar 2: Dm7 on beat 2 and 4
for beat in [1, 3]:
    time = 1.5 + beat * 0.375
    note = pretty_midi.Note(velocity=90, pitch=62, start=time, end=time + 0.125)  # D4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=65, start=time, end=time + 0.125)  # F4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.125)  # A4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.125)  # C4
    piano.notes.append(note)

# Bar 3: G7 on beat 2 and 4
for beat in [1, 3]:
    time = 2.5 + beat * 0.375
    note = pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.125)  # G4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.125)  # B4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.125)  # D4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=65, start=time, end=time + 0.125)  # F4
    piano.notes.append(note)

# Bar 4: Cm7 on beat 2 and 4
for beat in [1, 3]:
    time = 3.5 + beat * 0.375
    note = pretty_midi.Note(velocity=90, pitch=60, start=time, end=time + 0.125)  # C4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=63, start=time, end=time + 0.125)  # Eb4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=67, start=time, end=time + 0.125)  # G4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=71, start=time, end=time + 0.125)  # Bb4
    piano.notes.append(note)

# Bar 5: F7 on beat 2 and 4
for beat in [1, 3]:
    time = 4.5 + beat * 0.375
    note = pretty_midi.Note(velocity=90, pitch=65, start=time, end=time + 0.125)  # F4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=69, start=time, end=time + 0.125)  # A4
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=72, start=time, end=time + 0.125)  # C5
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=68, start=time, end=time + 0.125)  # Eb4
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D - E - F - A (D, E, F, A)
# Start on bar 2 (time 1.5), play first 3 notes (D, E, F), then on bar 4 (time 4.5) play A to resolve

# Bar 2: D, E, F
for i, pitch in enumerate([62, 64, 65]):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 4: A
note = pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625)
sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
