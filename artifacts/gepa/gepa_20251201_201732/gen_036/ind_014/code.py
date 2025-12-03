
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F - F, G, A, Bb, C, D, Eb, F
# Roots and fifths with chromatic approaches
# Bars 2-4 = 3 bars
bass_notes = [
    (1.5, 53),   # F2
    (1.875, 55),  # G2
    (2.25, 57),   # A2
    (2.625, 58),  # Bb2
    (3.0, 59),    # C2
    (3.375, 62),  # D2
    (3.75, 60),   # Eb2
    (4.125, 53),  # F2 (end of bar 2)
    (4.5, 53),    # F2
    (4.875, 55),  # G2
    (5.25, 57),   # A2
    (5.625, 58),  # Bb2
    (6.0, 59),    # C2
    (6.375, 62),  # D2
    (6.75, 60),   # Eb2
    (7.125, 53)   # F2 (end of bar 4)
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 - C, F, A, E
# Bar 3: Bb7 - F, Bb, D, Ab
# Bar 4: D7 - F, A, C, G
# Comp on 2 and 4

# Bar 2
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75)
piano.notes.append(note)  # C5
note = pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75)
piano.notes.append(note)  # F5
note = pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75)
piano.notes.append(note)  # A5
note = pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75)
piano.notes.append(note)  # E5

# Bar 3
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25)
piano.notes.append(note)  # F4
note = pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25)
piano.notes.append(note)  # Bb4
note = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25)
piano.notes.append(note)  # D4
note = pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.25)
piano.notes.append(note)  # Ab4

# Bar 4
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75)
piano.notes.append(note)  # F4
note = pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75)
piano.notes.append(note)  # A4
note = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75)
piano.notes.append(note)  # C4
note = pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75)
piano.notes.append(note)  # G4

# Dante: Tenor Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 - Motif starts
# F5, A5, Eb5, F5 (0.5s)
note = pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.75)
sax.notes.append(note)  # F5
note = pretty_midi.Note(velocity=110, pitch=79, start=1.75, end=2.0)
sax.notes.append(note)  # A5
note = pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25)
sax.notes.append(note)  # Eb5
note = pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.5)
sax.notes.append(note)  # F5

# Bar 3 - Let it hang, then come back
# Silence
# Bar 4 - Repeat and resolve
note = pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.75)
sax.notes.append(note)  # F5
note = pretty_midi.Note(velocity=110, pitch=79, start=4.75, end=5.0)
sax.notes.append(note)  # A5
note = pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25)
sax.notes.append(note)  # Eb5
note = pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.5)
sax.notes.append(note)  # F5

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
