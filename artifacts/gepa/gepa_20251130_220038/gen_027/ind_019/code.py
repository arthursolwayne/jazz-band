
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
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.75)),  # F
    (pretty_midi.Note(velocity=100, pitch=42, start=1.75, end=2.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.5)),  # C
    # Bar 3
    (pretty_midi.Note(velocity=100, pitch=39, start=2.5, end=2.75)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0)),  # A
    (pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.25)),  # Ab
    (pretty_midi.Note(velocity=100, pitch=36, start=3.25, end=3.5)),  # G
    # Bar 4
    (pretty_midi.Note(velocity=100, pitch=35, start=3.5, end=3.75)),  # F
    (pretty_midi.Note(velocity=100, pitch=34, start=3.75, end=4.0)),  # Eb
    (pretty_midi.Note(velocity=100, pitch=33, start=4.0, end=4.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=32, start=4.25, end=4.5)),  # C
    # Bar 4 (end)
    (pretty_midi.Note(velocity=100, pitch=31, start=4.5, end=4.75)),  # Bb
    (pretty_midi.Note(velocity=100, pitch=30, start=4.75, end=5.0)),  # A
    (pretty_midi.Note(velocity=100, pitch=29, start=5.0, end=5.25)),  # Ab
    (pretty_midi.Note(velocity=100, pitch=28, start=5.25, end=5.5)),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 on beat 2, Cm7 on beat 4
# Bar 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=2.0))  # Ab
# Bar 3
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=2.75, end=3.0))  # Ab
# Bar 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0))  # D

# Sax: your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, C
# Bar 2: F Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=58, start=1.75, end=2.0))  # Ab
# Bar 3: Bb C
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0))  # C
# Bar 4: F Ab
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=58, start=4.75, end=5.0))  # Ab

# Drums: continue for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
