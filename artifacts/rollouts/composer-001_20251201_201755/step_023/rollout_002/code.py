
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (F2-A2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # G2 (chromatic approach to A2) on beat 2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.125),
    # A2 (fifth) on beat 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    # F2 (root) on beat 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0),  # A (A5)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # E (E5)
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging
# F (D4) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # A (A4) on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.125),
    # C (C5) on beat 3
    pretty_midi.Note(velocity=110, pitch=76, start=2.125, end=2.5),
    # Leave it hanging on the last beat
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line (F2-A2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # A2 (fifth) on beat 1
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    # B2 (chromatic approach to C2) on beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.625),
    # C2 (root) on beat 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=4.0),
    # D2 (chromatic approach to E2) on beat 4
    pretty_midi.Note(velocity=100, pitch=40, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Bb (G4)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # F (F5)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # Ab (Ab5)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve it
# D (D4) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    # F (F4) on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.625),
    # G (G4) on beat 3
    pretty_midi.Note(velocity=110, pitch=71, start=3.625, end=4.0),
    # A (A4) on beat 4
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.375),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line (F2-A2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # E2 (chromatic approach to F2) on beat 1
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),
    # F2 (root) on beat 2
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.125),
    # G2 (chromatic approach to A2) on beat 3
    pretty_midi.Note(velocity=100, pitch=40, start=5.125, end=5.5),
    # A2 (fifth) on beat 4
    pretty_midi.Note(velocity=100, pitch=43, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # A (A5)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # E (E5)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
# F (F4) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),
    # A (A4) on beat 2
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.125),
    # C (C5) on beat 3
    pretty_midi.Note(velocity=110, pitch=76, start=5.125, end=5.5),
    # D (D5) on beat 4 (resolve to F)
    pretty_midi.Note(velocity=110, pitch=78, start=5.5, end=5.875),
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on beat 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on beat 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Kick on beat 3
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on beat 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.875),
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
