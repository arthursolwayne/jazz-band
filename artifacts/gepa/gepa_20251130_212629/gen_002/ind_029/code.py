
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
for i in range(4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.5 + 0.375)),  # D
    (pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=1.875 + 0.375)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.25 + 0.375)),  # C
    (pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=2.625 + 0.375)),  # D
    (pretty_midi.Note(velocity=100, pitch=52, start=2.999, end=2.999 + 0.375)),  # F
    (pretty_midi.Note(velocity=100, pitch=51, start=3.374, end=3.374 + 0.375)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=49, start=3.749, end=3.749 + 0.375)),  # C
    (pretty_midi.Note(velocity=100, pitch=50, start=4.124, end=4.124 + 0.375)),  # D
    (pretty_midi.Note(velocity=100, pitch=52, start=4.499, end=4.499 + 0.375)),  # F
    (pretty_midi.Note(velocity=100, pitch=51, start=4.874, end=4.874 + 0.375)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=49, start=5.249, end=5.249 + 0.375)),  # C
    (pretty_midi.Note(velocity=100, pitch=50, start=5.624, end=5.624 + 0.375))   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=1.875 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=1.875 + 0.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=1.875 + 0.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=1.875 + 0.125),  # C
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.375 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.375 + 0.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.375 + 0.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.375 + 0.125),  # C
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=4.875 + 0.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=4.875 + 0.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=4.875 + 0.125),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=4.875 + 0.125)   # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Dm7 motif: D, F, A, C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.125),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.625 + 0.125),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.75 + 0.125),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=1.875 + 0.125),  # C
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.0 + 0.125),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.125 + 0.125),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.25 + 0.125),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.375 + 0.125)   # C
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(6):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
