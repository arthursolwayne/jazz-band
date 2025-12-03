
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
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to C3 (MIDI 48) on beat 4
    pretty_midi.Note(velocity=90, pitch=47, start=2.375, end=2.625),
    # C3 (MIDI 48) on beat 4
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a D4 (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Chromatic approach to E4 (MIDI 64) on beat 2
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.0),
    # E4 (MIDI 64) on beat 3
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.375),
    # Leave it hanging on beat 4
    pretty_midi.Note(velocity=110, pitch=64, start=2.375, end=2.625),
    # Come back and finish it on beat 4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: C3 (MIDI 48) walking line with chromatic approaches
bass_notes = [
    # C3 (MIDI 48) on beat 1
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),
    # Chromatic approach to E3 (MIDI 52) on beat 2
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.625),
    # E3 (MIDI 52) on beat 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.625, end=3.875),
    # Chromatic approach to G3 (MIDI 55) on beat 4
    pretty_midi.Note(velocity=90, pitch=54, start=3.875, end=4.125),
    # G3 (MIDI 55) on beat 4
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    # Start with a G4 (MIDI 67) on beat 1
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    # Chromatic approach to A4 (MIDI 69) on beat 2
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.625),
    # A4 (MIDI 69) on beat 3
    pretty_midi.Note(velocity=110, pitch=69, start=3.625, end=3.875),
    # Leave it hanging on beat 4
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.125),
    # Come back and finish it on beat 4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: G3 (MIDI 55) walking line with chromatic approaches
bass_notes = [
    # G3 (MIDI 55) on beat 1
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),
    # Chromatic approach to B3 (MIDI 58) on beat 2
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.125),
    # B3 (MIDI 58) on beat 3
    pretty_midi.Note(velocity=100, pitch=58, start=5.125, end=5.375),
    # Chromatic approach to D4 (MIDI 62) on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=5.375, end=5.625),
    # D4 (MIDI 62) on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Start with a C4 (MIDI 60) on beat 1
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),
    # Chromatic approach to D4 (MIDI 62) on beat 2
    pretty_midi.Note(velocity=110, pitch=61, start=4.875, end=5.125),
    # D4 (MIDI 62) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.375),
    # Leave it hanging on beat 4
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.625),
    # Come back and finish it on beat 4
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
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
