
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
# Sax motif: Dm7 -> F7 -> Bb7 -> C7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.1875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.1875, end=2.375), # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5625, end=2.75), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),    # C
]
sax.notes.extend(sax_notes)

# Bass line: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.1875),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=2.1875, end=2.375), # G
    pretty_midi.Note(velocity=80, pitch=60, start=2.375, end=2.5625), # F
    pretty_midi.Note(velocity=80, pitch=57, start=2.5625, end=2.75), # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0),    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.25),  # A
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.3125, end=4.5),  # C
]
sax.notes.extend(sax_notes)

# Bass line: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.5625, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.3125), # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=4.3125, end=4.5),    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.25),  # A
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Bass line: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.0625, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.4375),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=5.8125), # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=5.8125, end=6.0),    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 4):
    start_time = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5))
    # Snare on 2 and 4
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875))
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0))
    # Hihat on every eighth
    for i in range(8):
        start = start_time + i * 0.1875
        end = start + 0.1875
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
