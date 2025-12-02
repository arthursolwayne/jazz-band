
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
# Sax: short motif, F Bb D G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=100, pitch=73, start=2.0625, end=2.25), # G
]
sax.notes.extend(sax_notes)

# Bass: walking line, F Ab Bb C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=90, pitch=44, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.0625), # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=2.0625, end=2.25), # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F A C Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.0), # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0), # Eb
    # Bar 2, beat 4: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375), # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375), # Ab
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat the motif, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=73, start=3.5625, end=3.75), # G
]
sax.notes.extend(sax_notes)

# Bass: walking line, G A Bb C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.1875), # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=3.5625, end=3.75), # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=73, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.5625), # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5625), # F
    # Bar 3, beat 4: C7 (C E G Bb)
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=3.875), # C
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=3.875), # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875), # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: end the motif with a suspension or a trill
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.6875), # G (suspension)
    pretty_midi.Note(velocity=100, pitch=71, start=4.6875, end=4.875), # F (resolution)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25), # Bb
]
sax.notes.extend(sax_notes)

# Bass: walking line, F G Ab Bb
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=90, pitch=46, start=5.0625, end=5.25), # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7 (F A C Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0625), # Eb
    # Bar 4, beat 4: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375), # D
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375), # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375), # Ab
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in [2, 3, 4]:
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
