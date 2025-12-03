
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # F (41) on 2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    # G2 (43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # Bb (45) on 4 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # D4 (62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # F4 (65) on beat 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),
    # D4 (62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),
    # Leave it hanging — no note on beat 4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C (40) on 1 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    # D2 (38) on 2
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    # F (41) on 3
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),
    # G2 (43) on 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif from bar 2, ending it on beat 4
sax_notes = [
    # F4 (65) on beat 1 (continuation)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),
    # D4 (62) on beat 2
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),
    # G4 (67) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    # C5 (69) on beat 4
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (38) on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    # F (41) on 2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),
    # G2 (43) on 3
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    # Bb (45) on 4 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C E G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One final phrase, return to D4 and end with a question
sax_notes = [
    # D4 (62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    # F4 (65) on beat 2
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),
    # D4 (62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),
    # G4 (67) on beat 4 (leaves it hanging)
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
