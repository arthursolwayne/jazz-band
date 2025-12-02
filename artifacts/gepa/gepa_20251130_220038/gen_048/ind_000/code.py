
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5s - 3.0s)
# Marcus - Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625), # D
    # Bar 2: Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=3.0), # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=3.0), # D
]
piano.notes.extend(piano_notes)

# Dante - Melody (Bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0), # E
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0s - 4.5s)
# Marcus - Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5), # D
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75), # D
    # Bar 3: Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.125), # D
]
piano.notes.extend(piano_notes)

# Dante - Melody (Bar 3)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5), # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5s - 6.0s)
# Marcus - Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25), # D
    # Bar 4: Dm7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625), # D
]
piano.notes.extend(piano_notes)

# Dante - Melody (Bar 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # F
]
sax.notes.extend(sax_notes)

# Drums for Bar 3 and 4
for bar in [3, 4]:
    start = (bar - 1) * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
