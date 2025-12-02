
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
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=34, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=36, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=35, start=2.25, end=2.625), # Gb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=34, start=2.625, end=3.0), # F

    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5), # A

    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0), # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75), # F (octave 3)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.75), # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75), # C
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75), # Eb
]
# Bar 3: Bb7 (Bb D F Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25), # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.25), # Ab
])
# Bar 4: C7 (C E G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75), # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # Bb
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (60) - Bb (62) - C (64) - F (60)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0), # F (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125), # F (return)
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
for i in [0, 2]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i * 0.75, end=1.5 + i * 0.75 + 0.375))
for i in [1, 3]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i * 0.75, end=1.5 + i * 0.75 + 0.375))
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.375))

# Bar 3 (3.0 - 4.5)
for i in [0, 2]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i * 0.75, end=3.0 + i * 0.75 + 0.375))
for i in [1, 3]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i * 0.75, end=3.0 + i * 0.75 + 0.375))
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.375))

# Bar 4 (4.5 - 6.0)
for i in [0, 2]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i * 0.75, end=4.5 + i * 0.75 + 0.375))
for i in [1, 3]:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5 + i * 0.75, end=4.5 + i * 0.75 + 0.375))
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
