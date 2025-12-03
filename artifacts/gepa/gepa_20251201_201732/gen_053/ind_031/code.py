
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
    # Hihat on every eighth
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

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: Walking line (roots and fifths with chromatic approaches)
bass_notes = [
    # F (root) with approach on beat 1
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    # G (fifth) with approach on beat 2
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),
    # Ab (chromatic approach to A)
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625),
    # A (third) with approach on beat 4
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=2.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # D (beat 1 of bar 2)
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.875),
    # Bb (beat 2 of bar 2)
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.25),
    # D (beat 3 of bar 2)
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.625),
    # F (beat 4 of bar 2)
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: (3.0 - 4.5s)
# Bass: Walking line (roots and fifths with chromatic approaches)
bass_notes = [
    # Bb (root) with approach on beat 1
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    # D (fifth) with approach on beat 2
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    # C# (chromatic approach to C)
    pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=4.125),
    # C (fourth) with approach on beat 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.5),
]
piano.notes.extend(piano_notes)

# Sax: Melody — continue the motif, leave it hanging
sax_notes = [
    # Bb (beat 1 of bar 3)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),
    # D (beat 2 of bar 3)
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),
    # C# (beat 3 of bar 3)
    pretty_midi.Note(velocity=110, pitch=73, start=3.75, end=4.125),
    # C (beat 4 of bar 3)
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: (4.5 - 6.0s)
# Bass: Walking line (roots and fifths with chromatic approaches)
bass_notes = [
    # F (root) with approach on beat 1
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),
    # G (fifth) with approach on beat 2
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),
    # Ab (chromatic approach to A)
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.625),
    # A (third) with approach on beat 4
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: Melody — finish it
sax_notes = [
    # D (beat 1 of bar 4)
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),
    # Bb (beat 2 of bar 4)
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),
    # D (beat 3 of bar 4)
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.625),
    # F (beat 4 of bar 4)
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
