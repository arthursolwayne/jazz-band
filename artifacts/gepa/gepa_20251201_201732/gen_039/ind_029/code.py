
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

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), chromatic approach from C#2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),
    # Bar 3: G2 (fifth), chromatic approach from F#2
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    # Bar 4: D2 (root), chromatic approach from C#2
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
]
# Bar 3: Bm7 (B-D-F#-A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),
])
# Bar 4: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - B (Dorian flavor, haunting and a bit dissonant)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
]
for note in sax_notes:
    sax.notes.append(note)

# Add remaining drum hits (fill the bar)
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5)

# Add the hihat on every eighth for all bars
for bar_start in [0.0, 1.5, 3.0, 4.5]:
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
