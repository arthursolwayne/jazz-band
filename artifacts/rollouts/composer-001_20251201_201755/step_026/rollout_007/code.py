
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875), # F (root)
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25), # Gb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Eb (root)
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.75), # F (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=35, start=3.75, end=4.125), # A (fifth)
    pretty_midi.Note(velocity=100, pitch=34, start=4.125, end=4.5),  # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Eb (root)
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25), # F (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=35, start=5.25, end=5.625), # A (fifth)
    pretty_midi.Note(velocity=100, pitch=34, start=5.625, end=6.0),  # Ab (chromatic approach)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25), # Ab
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0), # Ab
]

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75), # Bb
]

# Resolve on the last chord - Fm7 again
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=6.0), # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=6.0), # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=6.0), # C
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=6.0), # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (60), C (68), rest on 1, then repeat with a slight chromatic twist
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375), # F (repeat)
    pretty_midi.Note(velocity=110, pitch=59, start=3.375, end=3.75), # Gb (chromatic twist)
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875), # F (finish)
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=110, pitch=68, start=5.625, end=6.0),  # C (hold)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
