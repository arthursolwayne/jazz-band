
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
# Bass: F2 (MIDI 53), chromatic approach to G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.125),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),   # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.875),   # F#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # A (MIDI 82)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # E (MIDI 76)
]
piano.notes.extend(piano_notes)

# Sax: Motif
# Start with F (MIDI 71) on beat 1, then G (MIDI 72) on beat 2, then F on beat 3, leave it hanging on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=71, start=2.125, end=2.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 53), chromatic approach to G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.625, end=4.0),   # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.375),   # F#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),  # D (MIDI 74)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # F (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Ab (MIDI 71)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif with variation
# G (MIDI 72) on beat 1, A (MIDI 73) on beat 2, G on beat 3, leave it hanging on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=73, start=3.375, end=3.625),
    pretty_midi.Note(velocity=110, pitch=72, start=3.625, end=4.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (MIDI 53), chromatic approach to G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.125),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.125, end=5.5),   # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.875),   # F#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Bb (MIDI 67)
]
piano.notes.extend(piano_notes)

# Sax: Complete motif with resolution
# F (MIDI 71) on beat 1, G (MIDI 72) on beat 2, F on beat 3, resolve on F on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.125),
    pretty_midi.Note(velocity=110, pitch=71, start=5.125, end=5.5),
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.875),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and Bar 4 (3.0 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = 3.0 + bar * 1.5
    drum_notes = [
        # Kick on 1 and 3
        pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5),
        # Snare on 2 and 4
        pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0),
        # Hi-hat on every eighth
        pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=start_time + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.3125, end=start_time + 1.5),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
