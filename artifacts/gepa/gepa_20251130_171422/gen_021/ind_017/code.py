
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Rests and space to build tension
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=42, start=1.125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif
# Start with a simple, emotional motif in Dm
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25)) # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625)) # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0))  # D

# Bass line - chromatic, active, melodic
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75)) # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125)) # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5)) # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875)) # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25)) # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625)) # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0)) # Eb

# Piano chords - 7th chords, comp on 2 and 4
# Bar 2: Dm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875)) # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875)) # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875)) # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875)) # C

# Bar 3: Dm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625)) # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625)) # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625)) # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625)) # C

# Bar 4: Dm7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375)) # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375)) # F
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375)) # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375)) # C

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick_start = bar_start + 0.0
    snare_start = bar_start + 0.75
    kick_start2 = bar_start + 1.5
    snare_start2 = bar_start + 2.25
    hihat_start = bar_start
    hihat_start2 = bar_start + 0.375
    hihat_start3 = bar_start + 0.75
    hihat_start4 = bar_start + 1.125
    hihat_start5 = bar_start + 1.5
    hihat_start6 = bar_start + 1.875
    hihat_start7 = bar_start + 2.25
    hihat_start8 = bar_start + 2.625

    # Kicks
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start2, end=kick_start2 + 0.375))

    # Snares
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=snare_start, end=snare_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=snare_start2, end=snare_start2 + 0.375))

    # Hi-hats
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start2, end=hihat_start2 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start3, end=hihat_start3 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start4, end=hihat_start4 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start5, end=hihat_start5 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start6, end=hihat_start6 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start7, end=hihat_start7 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_start8, end=hihat_start8 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
