
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
for beat in [0.0, 0.75]:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + beat, end=bar1_start + beat + 0.15)
    drums.notes.append(kick)
for beat in [0.375, 1.125]:
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + beat, end=bar1_start + beat + 0.15)
    drums.notes.append(snare)
for beat in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + beat, end=bar1_start + beat + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bar2_start = 1.5
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 0.0, end=bar2_start + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=bar2_start + 0.25, end=bar2_start + 0.5), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 0.5, end=bar2_start + 0.75), # E
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 0.75, end=bar2_start + 1.0), # F
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 1.0, end=bar2_start + 1.25), # D
    pretty_midi.Note(velocity=90, pitch=60, start=bar2_start + 1.25, end=bar2_start + 1.5), # C
    pretty_midi.Note(velocity=90, pitch=59, start=bar2_start + 1.5, end=bar2_start + 1.75), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 1.75, end=bar2_start + 2.0), # D
    pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 2.0, end=bar2_start + 2.25), # E
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 2.25, end=bar2_start + 2.5), # F
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 2.5, end=bar2_start + 2.75), # G
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 2.75, end=bar2_start + 3.0), # F
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 3.0, end=bar2_start + 3.25), # D
    pretty_midi.Note(velocity=90, pitch=60, start=bar2_start + 3.25, end=bar2_start + 3.5), # C
    pretty_midi.Note(velocity=90, pitch=59, start=bar2_start + 3.5, end=bar2_start + 3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 3.75, end=bar2_start + 4.0), # D
    pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 4.0, end=bar2_start + 4.25), # E
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 4.25, end=bar2_start + 4.5), # F
    pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + 4.5, end=bar2_start + 4.75), # G
    pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + 4.75, end=bar2_start + 5.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping in Dm7
piano_notes = []
chord_d7 = [50, 52, 55, 57]  # Dm7 (D, F, A, C)
chord_g7 = [62, 64, 67, 69]  # G7 (G, B, D, F)
chord_cm7 = [60, 62, 65, 67]  # Cm7 (C, Eb, G, Bb)

for bar in range(2, 5):
    bar_start = (bar - 2) * 1.5 + bar2_start
    for note in chord_d7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 0.375, end=bar_start + 0.625))
    for note in chord_g7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 0.875, end=bar_start + 1.125))
    for note in chord_cm7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 1.375, end=bar_start + 1.625))
    for note in chord_d7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 1.875, end=bar_start + 2.125))
    for note in chord_g7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 2.375, end=bar_start + 2.625))
    for note in chord_cm7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 2.875, end=bar_start + 3.125))
    for note in chord_d7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 3.375, end=bar_start + 3.625))
    for note in chord_g7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 3.875, end=bar_start + 4.125))
    for note in chord_cm7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 4.375, end=bar_start + 4.625))
    for note in chord_d7:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar_start + 4.875, end=bar_start + 5.125))

piano.notes.extend(piano_notes)

# Sax: Motif in Dm, one phrase, sing it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 0.0, end=bar2_start + 0.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 0.25, end=bar2_start + 0.5),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 0.5, end=bar2_start + 0.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 0.75, end=bar2_start + 1.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 1.0, end=bar2_start + 1.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 1.25, end=bar2_start + 1.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 1.5, end=bar2_start + 1.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 1.75, end=bar2_start + 2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 2.0, end=bar2_start + 2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 2.25, end=bar2_start + 2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 2.5, end=bar2_start + 2.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 2.75, end=bar2_start + 3.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 3.0, end=bar2_start + 3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 3.25, end=bar2_start + 3.5),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 3.5, end=bar2_start + 3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 3.75, end=bar2_start + 4.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 4.0, end=bar2_start + 4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 4.25, end=bar2_start + 4.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 4.5, end=bar2_start + 4.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 4.75, end=bar2_start + 5.0),  # D
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dm_intro.mid")
