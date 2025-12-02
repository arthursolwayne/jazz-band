
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hats on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2–4: Full quartet (1.5 - 6.0s)
# Bass line: Walking, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.75)),  # F
    (pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0)),  # F#
    (pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25)),  # G
    (pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5)),  # G#
    (pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75)),  # A
    (pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0)),  # A#
    (pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.25)),  # B
    (pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.5)),  # C
    (pretty_midi.Note(velocity=90, pitch=58, start=3.5, end=3.75)),  # C#
    (pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0)),  # D
    (pretty_midi.Note(velocity=90, pitch=61, start=4.0, end=4.25)),  # D#
    (pretty_midi.Note(velocity=90, pitch=63, start=4.25, end=4.5)),  # E
    (pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75)),  # F
    (pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0)),  # F#
    (pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25)),  # G
    (pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.5)),  # G#
    (pretty_midi.Note(velocity=90, pitch=70, start=5.5, end=5.75)),  # A
    (pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0)),  # A#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2
chord_f7 = [53, 57, 60, 64]
for note in chord_f7:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=1.75, end=2.0))
# Bar 3: B7 on beat 2
chord_b7 = [62, 66, 69, 71]
for note in chord_b7:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=3.25, end=3.5))
# Bar 4: E7 on beat 2
chord_e7 = [59, 63, 66, 69]
for note in chord_e7:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=4.25, end=4.5))

# Sax: Tenor melody, start with a whisper, build into a cry
# Bar 2: F, G, A, Bb
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=95, pitch=70, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.5),  # Bb
    # Bar 3: Bb, A, G, F#
    pretty_midi.Note(velocity=85, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # F#
    # Bar 4: E, D, C#, B
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=95, pitch=65, start=4.0, end=4.25),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # B
]
sax.notes.extend(sax_notes)

# Drums: Bar 2–4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hats on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("dante_intro.mid")
