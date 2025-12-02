
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # G (Fm scale)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 3: Bbm7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # E
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 4: Ab7 (Ab, C, Eb, Gb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # Gb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
