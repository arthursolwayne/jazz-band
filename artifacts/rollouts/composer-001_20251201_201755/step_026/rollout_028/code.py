
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.6875),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=1.6875, end=2.0),  # F
    # Bar 3: C (fifth of F) with chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.1875),  # B
    pretty_midi.Note(velocity=100, pitch=77, start=2.1875, end=2.5),  # C
    # Bar 4: G (fifth of C) with chromatic approach from F#
    pretty_midi.Note(velocity=90, pitch=78, start=2.5, end=2.6875),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=2.6875, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=79, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (71) - A (74) - G (79) - F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=74, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=79, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),
    # Leave it hanging, then come back and finish it
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=79, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 3: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.5),  # F
    # Bar 4: C (fifth of F) with chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.6875),  # B
    pretty_midi.Note(velocity=100, pitch=77, start=3.6875, end=4.0),  # C
    # Bar 5: G (fifth of C) with chromatic approach from F#
    pretty_midi.Note(velocity=90, pitch=78, start=4.0, end=4.1875),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=4.1875, end=4.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=79, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),
    # Bar 5: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=77, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=81, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=79, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Sax: continue motif
# Motif: F (71) - A (74) - G (79) - F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=74, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=79, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.5),
    # Leave it hanging, then come back and finish it
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=74, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=79, start=4.25, end=4.375),
    pretty_midi.Note(velocity=110, pitch=71, start=4.375, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums continue
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bass: walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: F (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.6875, end=5.0),  # F
    # Bar 5: C (fifth of F) with chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.1875),  # B
    pretty_midi.Note(velocity=100, pitch=77, start=5.1875, end=5.5),  # C
    # Bar 6: G (fifth of C) with chromatic approach from F#
    pretty_midi.Note(velocity=90, pitch=78, start=5.5, end=5.6875),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=5.6875, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),
    # Bar 5: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=79, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),
    # Bar 6: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=77, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=81, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=79, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Sax: continue motif
# Motif: F (71) - A (74) - G (79) - F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=74, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=79, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),
    # Leave it hanging, then come back and finish it
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.625),
    pretty_midi.Note(velocity=110, pitch=74, start=5.625, end=5.75),
    pretty_midi.Note(velocity=110, pitch=79, start=5.75, end=5.875),
    pretty_midi.Note(velocity=110, pitch=71, start=5.875, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
