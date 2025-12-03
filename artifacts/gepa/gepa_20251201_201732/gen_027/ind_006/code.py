
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (F2) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=70, start=1.6875, end=1.875),
    # C (C3) with chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=75, start=2.0625, end=2.25),
    # Ab (Ab2) with chromatic approach from G
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=77, start=2.4375, end=2.625),
    # F (F2) again with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=70, start=2.8125, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.4375),
    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
]
drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (F4), Ab (Ab4), C (C5), F (F4)
# Play F on beat 1, Ab on beat 2, C on beat 3, leave F hanging on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=79, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=82, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=84, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=110, pitch=79, start=2.625, end=2.8125),
    # Repeat the motif, but end it cleanly
    pretty_midi.Note(velocity=110, pitch=79, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=82, start=3.1875, end=3.375),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
