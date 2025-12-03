
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) as root on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (MIDI 43) as fifth on 2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    # D# (MIDI 41) chromatic approach on 3
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),
    # D2 (MIDI 38) back to root on 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),  # A (MIDI 68)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C (MIDI 72)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Eb (MIDI 67)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: F (MIDI 65) on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    # Second note: Bb (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    # Third note: D (MIDI 69) on beat 3
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),
    # Leave it hanging at the end of the bar
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F# (MIDI 42) chromatic approach on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    # G (MIDI 43) as root on 2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),
    # Bb (MIDI 42) chromatic approach on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    # G (MIDI 43) back to root on 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # D (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab (MIDI 60)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve it
sax_notes = [
    # Continue the motif with a resolution
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # A (MIDI 45) chromatic approach on 1
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),
    # Bb (MIDI 46) as root on 2
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),
    # A# (MIDI 45) chromatic approach on 3
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625),
    # Bb (MIDI 46) back to root on 4
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F (MIDI 65)
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=6.0),  # A (MIDI 68)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C (MIDI 72)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Eb (MIDI 67)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif with a strong resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),
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

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
