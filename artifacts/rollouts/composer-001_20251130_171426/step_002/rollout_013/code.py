
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.0, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)
    drums.notes.append(hihat1)
    drums.notes.append(hihat2)
    drums.notes.append(hihat3)
    drums.notes.append(hihat4)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.25), # G#
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # C#
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0), # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875), # Eb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375), # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.0625, end=2.25), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.4375, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.8125, end=3.0), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.5625, end=3.75), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.9375, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.3125, end=4.5), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.0625, end=5.25), # C#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.8125, end=6.0), # C#
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
