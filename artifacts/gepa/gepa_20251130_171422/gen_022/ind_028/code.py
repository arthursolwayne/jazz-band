
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum sounds
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with hihat and snare, but leave a space before the kick
drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=0.0, end=0.15))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=0.3, end=0.45))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=0.6, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=0.9, end=1.05))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=1.2, end=1.35))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=1.35, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif in D minor with a touch of tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.65), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.65, end=1.8), # E
    pretty_midi.Note(velocity=100, pitch=60, start=1.8, end=1.95), # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.95, end=2.1), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.1, end=2.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4), # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.4, end=2.55), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.55, end=2.7), # G
]
sax.notes.extend(sax_notes)

# Bass line: chromatic walking line with melodic flair
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25), # E
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.5), # F
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75), # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Piano comping: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75), # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25), # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.25), # D
]
piano.notes.extend(piano_notes)

# Drums in bar 2: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=1.5, end=1.6))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=1.5, end=1.575))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=1.6, end=1.7))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=1.6, end=1.675))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=1.8, end=1.9))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=1.8, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=1.9, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=1.9, end=1.975))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=2.1, end=2.2))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=2.1, end=2.175))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=2.2, end=2.3))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=2.2, end=2.275))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=2.4, end=2.5))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=2.4, end=2.475))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=2.5, end=2.6))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=2.5, end=2.575))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=2.7, end=2.8))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=2.7, end=2.775))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=2.8, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=2.8, end=2.875))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif variation with space and a rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.15), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.15, end=3.3), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.3, end=3.45), # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.45, end=3.6), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.6, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9), # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.9, end=4.05), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.05, end=4.2), # G
]
sax.notes.extend(sax_notes)

# Bass line: chromatic walking line with a melodic twist
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25), # G
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75), # E
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0), # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.25), # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.25, end=4.5), # Eb
]
bass.notes.extend(bass_notes)

# Piano comping: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75), # D
]
piano.notes.extend(piano_notes)

# Drums in bar 3: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=3.0, end=3.1))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=3.0, end=3.075))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=3.1, end=3.2))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=3.1, end=3.175))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=3.3, end=3.4))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=3.3, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=3.4, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=3.4, end=3.475))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=3.6, end=3.7))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=3.6, end=3.675))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=3.7, end=3.8))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=3.7, end=3.775))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=3.9, end=4.0))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=3.9, end=3.975))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=4.0, end=4.1))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=4.0, end=4.075))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=4.2, end=4.3))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=4.2, end=4.275))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=4.3, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=4.3, end=4.375))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif resolution with a lingering note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.65), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.65, end=4.8), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.8, end=4.95), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.95, end=5.1), # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.1, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.4), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.4, end=5.55), # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.55, end=5.7), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.7, end=5.85), # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.85, end=6.0), # F
]
sax.notes.extend(sax_notes)

# Bass line: resolves to D with a chromatic descent
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75), # G
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5), # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.5, end=5.75), # D
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0), # C#
]
bass.notes.extend(bass_notes)

# Piano comping: 7th chords on 2 and 4 with a softer touch
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75), # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=70, pitch=62, start=5.0, end=5.25), # D
    pretty_midi.Note(velocity=70, pitch=67, start=5.0, end=5.25), # G
    pretty_midi.Note(velocity=70, pitch=69, start=5.0, end=5.25), # Bb
    pretty_midi.Note(velocity=70, pitch=71, start=5.0, end=5.25), # D
]
piano.notes.extend(piano_notes)

# Drums in bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=4.5, end=4.6))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=4.5, end=4.575))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=4.6, end=4.7))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=4.6, end=4.675))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=4.8, end=4.9))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=4.8, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=4.9, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=4.9, end=4.975))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=5.1, end=5.2))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=5.1, end=5.175))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=5.2, end=5.3))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=5.2, end=5.275))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=5.4, end=5.5))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=5.4, end=5.475))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=5.5, end=5.6))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=5.5, end=5.575))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=5.7, end=5.8))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=5.7, end=5.775))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=5.8, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=5.8, end=5.875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
