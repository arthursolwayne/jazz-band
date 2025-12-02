
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
    # Kick on 1 and 3 (beat 0 and 2)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    # Snare on 2 and 4 (beat 1 and 3)
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)
# Piano: 7th chords on 2 and 4 (beat 1 and 3)
piano_notes = [
    # D7 on beat 1 (F - A - C - D)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # D
    # G7 on beat 3 (F - Bb - D - G)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625), # G
]
piano.notes.extend(piano_notes)

# Bass: Walking line in F
bass_notes = [
    # F (beat 0)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # G (beat 1)
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    # Ab (beat 2)
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),
    # A (beat 3)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
    # Bb (beat 4)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    # C (beat 5)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    # D (beat 6)
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),
    # Eb (beat 7)
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Drums: Bar 2
for i in range(2):
    start = 1.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375), # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375), # Hi-hat
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125), # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5), # Snare on 4
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Sax: Bar 2 (start of motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.75, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0), # A
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Piano: 7th chords on 2 and 4 (beat 1 and 3)
piano_notes = [
    # C7 on beat 1 (F - A - C - E)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375), # E
    # G7 on beat 3 (F - Bb - D - G)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125), # G
]
piano.notes.extend(piano_notes)

# Bass: Walking line in F
bass_notes = [
    # A (beat 4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    # Bb (beat 5)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    # C (beat 6)
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),
    # D (beat 7)
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),
    # E (beat 8)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),
    # F (beat 9)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    # G (beat 10)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    # Ab (beat 11)
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Drums: Bar 3
for i in range(2):
    start = 3.0 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375), # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375), # Hi-hat
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125), # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5), # Snare on 4
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Sax: Bar 3 (continue motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0), # A
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
# Piano: 7th chords on 2 and 4 (beat 1 and 3)
piano_notes = [
    # G7 on beat 1 (F - Bb - D - G)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875), # G
    # C7 on beat 3 (F - A - C - E)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625), # E
]
piano.notes.extend(piano_notes)

# Bass: Walking line in F
bass_notes = [
    # Eb (beat 12)
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),
    # F (beat 13)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    # G (beat 14)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    # Ab (beat 15)
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Drums: Bar 4
for i in range(2):
    start = 4.5 + i * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375), # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375), # Hi-hat
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125), # Kick on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5), # Snare on 4
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Sax: Bar 4 (finish motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5), # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0), # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
