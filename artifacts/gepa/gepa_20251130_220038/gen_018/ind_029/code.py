
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Time (in seconds)
bar_start = 0.0
bar_duration = 1.5
beat_duration = 0.375  # 160 BPM, 4/4 time

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Snare on 2 and 4, hihat on every eighth, kick on 1 and 3
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 0.75, end=bar_start + 0.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=snare, start=bar_start + 1.125, end=bar_start + 1.125 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start, end=bar_start + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 0.375, end=bar_start + 0.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 0.75, end=bar_start + 0.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 1.125, end=bar_start + 1.125 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 1.5, end=bar_start + 1.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 1.875, end=bar_start + 1.875 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 2.25, end=bar_start + 2.25 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 2.625, end=bar_start + 2.625 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 3.0, end=bar_start + 3.0 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 3.375, end=bar_start + 3.375 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 3.75, end=bar_start + 3.75 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 4.125, end=bar_start + 4.125 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 4.5, end=bar_start + 4.5 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 4.875, end=bar_start + 4.875 + 0.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=bar_start + 5.25, end=bar_start + 5.25 + 0.125),

    # Kick on 1 and 3 of bar 1 (0.0 and 0.75 on bar_start)
    pretty_midi.Note(velocity=100, pitch=kick, start=bar_start, end=bar_start + 0.125),
    pretty_midi.Note(velocity=100, pitch=kick, start=bar_start + 0.75, end=bar_start + 0.75 + 0.125),
])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)),  # D (root)
    (pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=1.875 + 0.375)),  # Eb (chromatic)
    (pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.25 + 0.375)),  # E (up approach)
    (pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.625 + 0.375)),  # D (back to root)
]

bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4 (D7 on beat 2, A7 on beat 4)
piano_notes = [
    # D7 on beat 2 (1.875)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=1.875 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.875 + 0.125),  # A (7th)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=1.875 + 0.125),  # F# (3rd)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=1.875 + 0.125),  # C# (5th),

    # A7 on beat 4 (2.625)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.625 + 0.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.625 + 0.125),  # E (7th)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.625 + 0.125),  # C (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.625 + 0.125),  # G (5th)
]

piano.notes.extend(piano_notes)

# Sax: Dante (tenor), short motif that "sings" — D, Eb, E, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.625 + 0.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.75 + 0.125),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=1.875 + 0.125),  # D (resolve)
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375)),  # D (root)
    (pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.375 + 0.375)),  # Eb (chromatic)
    (pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.75 + 0.375)),  # E (up approach)
    (pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.125 + 0.375)),  # D (back to root)
]

bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4 (D7 on beat 2, A7 on beat 4)
piano_notes = [
    # D7 on beat 2 (3.375)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.375 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.375 + 0.125),  # A (7th)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.375 + 0.125),  # F# (3rd)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.375 + 0.125),  # C# (5th),

    # A7 on beat 4 (4.125)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.125 + 0.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.125 + 0.125),  # E (7th)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.125 + 0.125),  # C (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.125 + 0.125),  # G (5th)
]

piano.notes.extend(piano_notes)

# Sax: Dante, repeat the motif with a slight variation — D, Eb, E, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.125, end=3.125 + 0.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.25 + 0.125),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.375 + 0.125),  # D (resolve)
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375)),  # D (root)
    (pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=4.875 + 0.375)),  # Eb (chromatic)
    (pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.25 + 0.375)),  # E (up approach)
    (pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.625 + 0.375)),  # D (back to root)
]

bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4 (D7 on beat 2, A7 on beat 4)
piano_notes = [
    # D7 on beat 2 (4.875)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=4.875 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=4.875 + 0.125),  # A (7th)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=4.875 + 0.125),  # F# (3rd)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=4.875 + 0.125),  # C# (5th),

    # A7 on beat 4 (5.625)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.625 + 0.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.625 + 0.125),  # E (7th)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.625 + 0.125),  # C (3rd)
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=5.625 + 0.125),  # G (5th)
]

piano.notes.extend(piano_notes)

# Sax: Dante, repeat the motif again, but with a slight dynamic shift (fading out)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.625, end=4.625 + 0.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.75 + 0.125),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=4.875 + 0.125),  # D (resolve)
]

sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
