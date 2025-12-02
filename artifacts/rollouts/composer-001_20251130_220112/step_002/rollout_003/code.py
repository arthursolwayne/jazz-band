
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125, 3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125, 4.5, 4.6875, 4.875, 5.0625, 5.25]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 62), # D
    (1.75, 60), # Bb
    (2.0, 62), # D
    (2.25, 64), # F
    (2.5, 66), # G
    (2.75, 64), # F
    (3.0, 62), # D
    (3.25, 60), # Bb
    (3.5, 62), # D
    (3.75, 64), # F
    (4.0, 65), # F#
    (4.25, 64), # F
    (4.5, 62), # D
    (4.75, 60), # Bb
    (5.0, 62), # D
    (5.25, 64), # F
    (5.5, 66), # G
    (5.75, 64), # F
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=t, end=t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    (1.5, 62), # D7: D, F#, A, C
    (1.5, 67), # F#
    (1.5, 71), # A
    (1.5, 64), # C
    # Bar 3 (2.5 - 3.0s)
    (2.5, 62), # D7
    (2.5, 67),
    (2.5, 71),
    (2.5, 64),
    # Bar 4 (3.5 - 4.0s)
    (3.5, 62), # D7
    (3.5, 67),
    (3.5, 71),
    (3.5, 64),
]

for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.25)
    piano.notes.append(note)

# Sax: motif - start it, leave it hanging, come back and finish it
# Dm6/9 - motif: D, F, G, Bb
sax_notes = [
    # Bar 2 (1.5 - 1.75s)
    (1.5, 62), # D
    (1.5, 64), # F
    (1.5, 67), # G
    (1.5, 60), # Bb
    # Bar 3 (2.5 - 2.75s)
    (2.5, 62), # D
    (2.5, 64), # F
    (2.5, 67), # G
    (2.5, 60), # Bb
    # Bar 4 (3.5 - 3.75s)
    (3.5, 62), # D
    (3.5, 64), # F
    (3.5, 67), # G
    (3.5, 60), # Bb
]

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
