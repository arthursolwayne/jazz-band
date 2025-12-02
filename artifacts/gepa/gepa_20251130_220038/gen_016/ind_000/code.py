
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Upright Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum samples
kick = 36  # Kick drum
snare = 38 # Snare
hihat = 42 # Closed hihat

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    (kick, 0.0), (snare, 0.75), (kick, 1.125), (snare, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 2-4: Full quartet (1.5s - 6.0s)

# Drums: same pattern, shifted to start at 1.5s
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + 1.5, end=time + 1.75))

# Bass: Walking line in Fm7 (F, Ab, Bb, D), with chromatic approach
# Start on 1.5s
bass_notes = [
    (37, 1.5),   # F (pitch 37)
    (35, 2.0),   # Eb (approach to Ab)
    (41, 2.25),  # Ab
    (40, 2.75),  # G (approach to Bb)
    (42, 3.0),   # Bb
    (39, 3.5),   # G# (approach to D)
    (45, 3.75),  # D
    (44, 4.25),  # C# (approach to F)
    (37, 4.5),   # F
    (35, 5.0),   # Eb (approach to Ab)
    (41, 5.25),  # Ab
    (40, 5.75),  # G (approach to Bb)
    (42, 6.0)    # Bb
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, D
# Bb7 = Bb, D, F, Ab
# Fm7 = F, Ab, C, D
# Bb7 = Bb, D, F, Ab

# Bar 2: Fm7 (1.5s - 2.0s)
# Bar 3: Bb7 (2.5s - 3.0s)
# Bar 4: Fm7 (3.5s - 4.0s)
# Bar 4: Bb7 (4.5s - 5.0s)

piano_notes = [
    # Fm7 at 1.5s (chord on 2)
    (37, 1.5), (41, 1.5), (51, 1.5), (45, 1.5),  # F, Ab, C, D
    # Bb7 at 2.5s (chord on 4)
    (42, 2.5), (45, 2.5), (37, 2.5), (41, 2.5),  # Bb, D, F, Ab
    # Fm7 at 3.5s (chord on 2)
    (37, 3.5), (41, 3.5), (51, 3.5), (45, 3.5),
    # Bb7 at 4.5s (chord on 4)
    (42, 4.5), (45, 4.5), (37, 4.5), (41, 4.5)
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Melody - motif starts at 1.5s
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F -> Ab -> Bb -> F (a suspended, haunting phrase)
sax_notes = [
    (37, 1.5),   # F
    (41, 1.75),  # Ab
    (42, 2.0),   # Bb
    (37, 2.5),   # F
    (37, 3.0),   # F (hold)
    (41, 3.25),  # Ab
    (42, 3.5),   # Bb
    (37, 4.0),   # F
    (37, 4.5),   # F (hold)
    (41, 4.75),  # Ab
    (42, 5.0),   # Bb
    (37, 5.5)    # F
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dantes_intro.mid")
