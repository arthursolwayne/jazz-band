
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F (F2, A2, C3, D3, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=90, pitch=58, start=2.625, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G (Fmaj7 3rd)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # E (Fmaj7 7th)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # G again
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # A (Fmaj7 9th)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F (F2, A2, C3, D3, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmaj7 (Bb, D, F, A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # A
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # E
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F (F2, A2, C3, D3, etc.)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dmin7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Same pattern as bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
