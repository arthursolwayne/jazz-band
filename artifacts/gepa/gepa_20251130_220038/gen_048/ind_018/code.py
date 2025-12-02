
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Marcus - Walking bass line (F7 chord: F, A, C, E)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F (70)
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # G (72)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # E (69)
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0), # F# (71)
]

bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4 (F7: F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=2.25), # F
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=2.25), # G
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=2.25), # E
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=2.25), # A
    pretty_midi.Note(velocity=95, pitch=70, start=2.25, end=3.0), # F
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=3.0), # G
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=3.0), # E
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=3.0), # A
]

piano.notes.extend(piano_notes)

# Dante - Motif: F, G#, A, Bb (rest, then cry)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=70, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=105, pitch=73, start=1.875, end=2.25), # G#
    pretty_midi.Note(velocity=105, pitch=71, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=105, pitch=70, start=2.625, end=3.0), # F
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus - Walking bass line (F7 chord: F, A, C, E)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5), # F
]

bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4 (F7: F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=3.75), # F
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.75), # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.75), # E
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.75), # A
    pretty_midi.Note(velocity=95, pitch=70, start=3.75, end=4.5), # F
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.5), # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.5), # E
    pretty_midi.Note(velocity=95, pitch=74, start=3.75, end=4.5), # A
]

piano.notes.extend(piano_notes)

# Dante - Motif variation: F, Bb, E, rest (builds tension)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=70, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=105, pitch=68, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=105, pitch=69, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=105, pitch=70, start=4.125, end=4.5), # F
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus - Walking bass line (F7 chord: F, A, C, E)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0), # F#
]

bass.notes.extend(bass_notes)

# Diane - 7th chords on 2 and 4 (F7: F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=70, start=4.5, end=5.25), # F
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=5.25), # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=5.25), # E
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=5.25), # A
    pretty_midi.Note(velocity=95, pitch=70, start=5.25, end=6.0), # F
    pretty_midi.Note(velocity=95, pitch=72, start=5.25, end=6.0), # G
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=6.0), # E
    pretty_midi.Note(velocity=95, pitch=74, start=5.25, end=6.0), # A
]

piano.notes.extend(piano_notes)

# Dante - Motif resolution: F, G#, rest, Bb
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=70, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=105, pitch=73, start=4.875, end=5.25), # G#
    pretty_midi.Note(velocity=105, pitch=68, start=5.625, end=6.0), # Bb
]

sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 * bar
    drum_notes = [
        # Kick on 1
        pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
        # Snare on 2
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
        # Kick on 3
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
        # Snare on 4
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
        # Hihat on every eighth
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),
    ]
    drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write('dante_intro.mid')
