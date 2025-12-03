
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (F) on beat 1
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    # Bb (fifth) on beat 2
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),
    # D (chromatic approach up) on beat 3
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    # F (root) on beat 4
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a descending triplet on Fm7
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # F
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # F
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.375),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bb (fifth) on beat 1
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),
    # F (root) on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),
    # Ab (chromatic approach down) on beat 3
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),
    # Bb (fifth) on beat 4
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Ab7 (Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif with a call and response
sax_notes = [
    # Call with a descending triplet on Ab7
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.375),  # Ab
    # Response with an ascending triplet
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.625, end=3.75),  # C
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F (root) on beat 1
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),
    # Ab (chromatic approach up) on beat 2
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),
    # Bb (fifth) on beat 3
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),
    # F (root) on beat 4
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif with a resolution
sax_notes = [
    # Resolution with a descending triplet on Fm7
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=4.875),  # F
    # End on F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
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

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Out of range but needed for the last beat
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

# Save the MIDI file
# midi.write disabled
