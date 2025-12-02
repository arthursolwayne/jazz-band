
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) - G (fifth) with chromatic approach on E#
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # E#2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # D2 (approach to F)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.0),  # F2
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # A2
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=2.0),  # C3
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.0),  # E3
]
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing
# Motif: F - G - E - F (F, G, E, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=3.0),  # F2
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 3: Bb (root) - D (fifth) with chromatic approach on A#
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.125),  # A#2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),  # G2 (approach to Bb)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Bbmin7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Bb2
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),  # D2
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.5),  # F2
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),  # Ab2
]
piano.notes.extend(piano_notes)

# Sax: motif continuation, leave it hanging
# Motif: Bb - C - A - Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # C2
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # Bb2
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: C (root) - E (fifth) with chromatic approach on D#
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # E2
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.625),  # D#2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),  # B2 (approach to C)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # C2
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),  # E2
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),  # G2
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.0),  # B2
]
piano.notes.extend(piano_notes)

# Sax: finish the motif, come back and finish it
# Motif: C - D - B - C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.625),  # B2
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # C2
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
