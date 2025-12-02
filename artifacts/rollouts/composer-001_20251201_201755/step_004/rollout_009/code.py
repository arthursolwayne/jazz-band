
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F2 (root), G2 (fifth), F#2 (chromatic approach), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),
]
piano.notes.extend(piano_notes)

# Bar 3: F7 (F, A, C, E flat)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Play a motif starting on F, then phrase it with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Bass (walking line, F2 - C3)
bass_notes = [
    # Bar 3: F2 (root), G2 (fifth), F#2 (chromatic approach), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (walking line, F2 - C3)
bass_notes = [
    # Bar 4: F2 (root), G2 (fifth), F#2 (chromatic approach), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Bar 4: Sax (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
