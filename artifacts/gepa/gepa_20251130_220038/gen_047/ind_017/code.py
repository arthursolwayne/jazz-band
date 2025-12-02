
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25)),  # C
    (pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)),  # D
    (pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75)),  # E
    (pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0)),  # D
    (pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25)),  # C
    (pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.5)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75)),  # C
    (pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)),  # D
    (pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.25)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5)),  # C
    (pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)),  # D
    (pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0)),  # E
    (pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5)),  # C
    (pretty_midi.Note(velocity=100, pitch=59, start=5.5, end=5.75)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0)),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Motif - Dm7 to G7 to Cm7, then a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),   # D
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=76, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.5),   # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=110, pitch=76, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=110, pitch=77, start=4.25, end=4.5),   # G
    pretty_midi.Note(velocity=110, pitch=79, start=4.5, end=4.75),   # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),   # E
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),   # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for beat in range(4):
        time = (bar * 1.5) + (beat * 0.375)
        if beat % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
