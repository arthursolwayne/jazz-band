
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
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=1.6875, end=1.875),  # E2 (chromatic approach)
    # Bar 2: C3 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=81, start=1.875, end=2.0625),  # C3
    pretty_midi.Note(velocity=80, pitch=82, start=2.0625, end=2.25),  # C#3 (chromatic approach)
    # Bar 3: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.4375),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=2.4375, end=2.625),  # E2 (chromatic approach)
    # Bar 3: C3 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=2.8125),  # C3
    pretty_midi.Note(velocity=80, pitch=82, start=2.8125, end=3.0),  # C#3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # F2
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0),  # C3
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=88, start=1.5, end=3.0),  # A3
    # Bar 3: Bb7 (Bb D F Ab) - open voicing
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # Bb2
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=3.0),  # D3
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=89, start=2.25, end=3.0),  # Ab3
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (short motif, leave it hanging on Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.6875),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=1.6875, end=1.875),  # Bb2
    pretty_midi.Note(velocity=110, pitch=78, start=1.875, end=2.0625),  # C3
    pretty_midi.Note(velocity=110, pitch=76, start=2.0625, end=2.25),  # F2
    # Leave it hanging on Bb for a moment
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.4375),  # Bb2
    pretty_midi.Note(velocity=110, pitch=76, start=2.4375, end=2.625),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=2.625, end=2.8125),  # Bb2
    pretty_midi.Note(velocity=110, pitch=78, start=2.8125, end=3.0),  # C3
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 4: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.1875),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=3.1875, end=3.375),  # E2 (chromatic approach)
    # Bar 4: C3 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.5625),  # C3
    pretty_midi.Note(velocity=80, pitch=82, start=3.5625, end=3.75),  # C#3 (chromatic approach)
    # Bar 5: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=3.9375),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=3.9375, end=4.125),  # E2 (chromatic approach)
    # Bar 5: C3 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=81, start=4.125, end=4.3125),  # C3
    pretty_midi.Note(velocity=80, pitch=82, start=4.3125, end=4.5),  # C#3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=4.5),  # G2
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=4.5),  # B2
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=4.5),  # D3
    pretty_midi.Note(velocity=100, pitch=88, start=3.0, end=4.5),  # F3
    # Bar 5: C7 (C E G B) - open voicing
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5),  # C2
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.5),  # E2
    pretty_midi.Note(velocity=100, pitch=86, start=3.75, end=4.5),  # G2
    pretty_midi.Note(velocity=100, pitch=88, start=3.75, end=4.5),  # B2
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
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

# Sax: Continue the motif
# Motif continuation: F - Bb - C - F (finish the motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.1875),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=3.1875, end=3.375),  # Bb2
    pretty_midi.Note(velocity=110, pitch=78, start=3.375, end=3.5625),  # C3
    pretty_midi.Note(velocity=110, pitch=76, start=3.5625, end=3.75),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=3.75, end=3.9375),  # Bb2
    pretty_midi.Note(velocity=110, pitch=78, start=3.9375, end=4.125),  # C3
    pretty_midi.Note(velocity=110, pitch=76, start=4.125, end=4.3125),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=4.3125, end=4.5),  # Bb2
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 6: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=4.6875, end=4.875),  # E2 (chromatic approach)
    # Bar 6: C3 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.0625),  # C3
    pretty_midi.Note(velocity=80, pitch=82, start=5.0625, end=5.25),  # C#3 (chromatic approach)
    # Bar 7: F2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.4375),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=5.4375, end=5.625),  # E2 (chromatic approach)
    # Bar 7: C3 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=5.8125),  # C3
    pretty_midi.Note(velocity=80, pitch=82, start=5.8125, end=6.0),  # C#3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 6: C7 (C E G B) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # C2
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # E2
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=6.0),  # G2
    pretty_midi.Note(velocity=100, pitch=88, start=4.5, end=6.0),  # B2
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
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

# Sax: Final resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.6875),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=4.6875, end=4.875),  # Bb2
    pretty_midi.Note(velocity=110, pitch=78, start=4.875, end=5.0625),  # C3
    pretty_midi.Note(velocity=110, pitch=76, start=5.0625, end=5.25),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.4375),  # Bb2
    pretty_midi.Note(velocity=110, pitch=78, start=5.4375, end=5.625),  # C3
    pretty_midi.Note(velocity=110, pitch=76, start=5.625, end=5.8125),  # F2
    pretty_midi.Note(velocity=110, pitch=77, start=5.8125, end=6.0),  # Bb2
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
