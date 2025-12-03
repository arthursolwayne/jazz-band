
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4,
                                                      time=0,螃蟹=0)]

# Define the key: Dm (D minor)
# Scale degrees: D, Eb, F, G, Ab, Bb, C
# We'll use Dm7 as the base chord: D, F, A, C
# We'll use Dm7, Gm7, Cm7, F7 for the chord progression

# Define instruments
# Tenor Sax (MIDI channel 1)
tenor_sax = pretty_midi.Instrument(program=64)
pm.instruments.append(tenor_sax)

# Bass (MIDI channel 2)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# Piano (MIDI channel 0)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# Drums (MIDI channel 9)
drums = pretty_midi.Instrument(program=9)
pm.instruments.append(drums)

# Define the time per bar in seconds (160 BPM = 60/160 = 0.375 seconds per beat)
beats_per_bar = 4
time_per_beat = 60.0 / 160.0
time_per_bar = beats_per_bar * time_per_beat

#-------------------
# DRUMS: Little Ray
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use standard MIDI drum notes
# Kick = 36, Snare = 38, Hihat = 42

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

#-------------------
# BASS: Marcus
# Walking line: D2-G2, roots and fifths with chromatic approaches

# D (MIDI 62) -> Eb (63) -> F (64) -> G (65)
# D -> Eb (chromatic), G (fifth), A (root), Bb (chromatic), C (fifth)
# Bar 1: D, Eb, G, A
# Bar 2: Bb, C, D, Eb
# Bar 3: F, G, A, Bb
# Bar 4: C, D, Eb, F

# Bar 1 (D, Eb, G, A)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=0.0, end=0.375))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=0.375, end=0.75))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0.75, end=1.125))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.125, end=1.5))

# Bar 2 (Bb, C, D, Eb)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0))

# Bar 3 (F, G, A, Bb)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5))

# Bar 4 (C, D, Eb, F)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0))

#-------------------
# PIANO: Diane
# Open voicings, different chord each bar, resolve on the last
# Bar 1: Dm7 (D, F, A, C)
# Bar 2: Gm7 (G, Bb, D, F)
# Bar 3: Cm7 (C, Eb, G, Bb)
# Bar 4: F7 (F, A, C, E)

# Bar 1: Dm7 at beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=68, start=1.5, end=1.75))  # D4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75))  # F4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.75))  # A4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.75))  # C5

# Bar 2: Gm7 at beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.25))  # G4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=3.0, end=3.25))  # Bb4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=3.0, end=3.25))  # D5
piano.notes.append(pretty_midi.Note(velocity=80, pitch=83, start=3.0, end=3.25))  # F5

# Bar 3: Cm7 at beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.75))  # C4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.75))  # Eb4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=78, start=4.5, end=4.75))  # G4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=4.5, end=4.75))  # Bb4

# Bar 4: F7 at beat 2
piano.notes.append(pretty_midi.Note(velocity=80, pitch=77, start=6.0, end=6.25))  # F4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=80, start=6.0, end=6.25))  # A4
piano.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=6.0, end=6.25))  # C5
piano.notes.append(pretty_midi.Note(velocity=80, pitch=86, start=6.0, end=6.25))  # E5

#-------------------
# TENOR SAX: Dante
# One short motif, start it, leave it hanging, come back and finish it.
# No scale runs. Make it sing.

# First bar: motif starts on beat 1
# D4 (MIDI 62) on beat 1
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=0.0, end=0.375))

# Bar 2: leave it hanging — nothing on the first two beats
# End the motif on beat 3
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.125, end=1.5))

# Bar 3: continue the motif in a new direction
# G4 (MIDI 67) on beat 1
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375))

# Bar 4: resolve the motif — return to D4
tenor_sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875))

# Save the MIDI file
pm.write('dante_intro.mid')
