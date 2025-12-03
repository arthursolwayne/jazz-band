
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on beat 1
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43) on beat 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # G2 (MIDI 43) on beat 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to A2 (MIDI 45) on beat 4
    pretty_midi.Note(velocity=80, pitch=44, start=2.375, end=2.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=75, pitch=69, start=1.5, end=2.0),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    # D4 (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    # F#4 (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),
    # A4 (MIDI 71) on beat 3
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.1875),
    # Leave it hanging on the last beat
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: G2 (MIDI 43) walking line with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on beat 1
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # Chromatic approach to A2 (MIDI 45) on beat 2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.5),
    # A2 (MIDI 45) on beat 3
    pretty_midi.Note(velocity=90, pitch=45, start=3.5, end=3.875),
    # Chromatic approach to B2 (MIDI 47) on beat 4
    pretty_midi.Note(velocity=80, pitch=46, start=3.875, end=4.0)
]
bass.notes.extend(bass_notes)

# Piano: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.5),  # F#4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=75, pitch=69, start=3.0, end=3.5),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, finish it
sax_notes = [
    # D4 (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),
    # F#4 (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),
    # A4 (MIDI 71) on beat 3
    pretty_midi.Note(velocity=110, pitch=71, start=3.5, end=3.6875),
    # D5 (MIDI 72) on beat 4 to finish the motif
    pretty_midi.Note(velocity=110, pitch=72, start=3.875, end=4.0)
]
sax.notes.extend(sax_notes)

# Drums: Repeat the same pattern
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: B2 (MIDI 47) walking line with chromatic approaches
bass_notes = [
    # B2 (MIDI 47) on beat 1
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),
    # Chromatic approach to C3 (MIDI 48) on beat 2
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.0),
    # C3 (MIDI 48) on beat 3
    pretty_midi.Note(velocity=90, pitch=48, start=5.0, end=5.375),
    # Chromatic approach to D3 (MIDI 50) on beat 4
    pretty_midi.Note(velocity=80, pitch=49, start=5.375, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=85, pitch=65, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=75, pitch=69, start=4.5, end=5.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Repeat the motif, but end it on D5 (MIDI 72)
sax_notes = [
    # D4 (MIDI 62) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    # F#4 (MIDI 67) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),
    # A4 (MIDI 71) on beat 3
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.1875),
    # D5 (MIDI 72) on beat 4 to finish the motif
    pretty_midi.Note(velocity=110, pitch=72, start=5.375, end=5.5)
]
sax.notes.extend(sax_notes)

# Drums: Repeat the same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
