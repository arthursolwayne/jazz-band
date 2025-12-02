
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

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36),  # kick on 1
    (0.375, 42), # hihat on 2
    (0.75, 38),  # snare on 2
    (1.125, 42), # hihat on 3
    (1.5, 36),   # kick on 3
    (1.875, 42), # hihat on 4
    (2.25, 38),  # snare on 4
    (2.625, 42)  # hihat on 4
]
for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62),  # D (root)
    (1.875, 60), # C (chromatic approach)
    (2.25, 64),  # F (3rd)
    (2.625, 62), # D (root)
    (2.875, 60), # C (chromatic approach)
    (3.25, 65),  # G (5th)
    (3.625, 62), # D (root)
    (4.0, 60),   # C (chromatic approach)
    (4.375, 64), # F (3rd)
    (4.75, 62),  # D (root)
    (5.125, 60), # C (chromatic approach)
    (5.5, 65),   # G (5th)
    (5.875, 62)  # D (root)
]
for time, note in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    (1.5, 62),  # D
    (1.5, 67),  # Bb
    (1.875, 62), # D
    (1.875, 67), # Bb
    # Bar 3 (2.25 - 3.0s)
    (2.25, 62),  # D
    (2.25, 67),  # Bb
    (2.625, 62), # D
    (2.625, 67), # Bb
    # Bar 4 (3.0 - 3.75s)
    (3.0, 62),   # D
    (3.0, 67),   # Bb
    (3.375, 62), # D
    (3.375, 67), # Bb
    # Bar 4 (3.75 - 4.5s)
    (3.75, 62),  # D
    (3.75, 67),  # Bb
    (4.125, 62), # D
    (4.125, 67), # Bb
    # Bar 4 (4.5 - 5.25s)
    (4.5, 62),   # D
    (4.5, 67),   # Bb
    (4.875, 62), # D
    (4.875, 67), # Bb
]
for time, note in piano_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125)
    piano.notes.append(note)

# Sax: Motif with a question, start on D, leave it hanging
sax_notes = [
    (1.5, 62),   # D
    (1.75, 65),  # F
    (2.0, 62),   # D
    (2.5, 65),   # F
    (2.75, 67),  # G
    (3.0, 62),   # D
    (3.5, 65),   # F
    (3.75, 67),  # G
    (4.0, 63),   # Eb (chromatic approach)
    (4.25, 65),  # F
    (4.5, 63),   # Eb
    (5.0, 65),   # F
    (5.25, 67),  # G
    (5.5, 62)    # D
]
for time, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
