
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
bar_length = 1.5
for time in [0.0, 0.75]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.25)
    drums.notes.append(note)
for time in [0.0, 0.75]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.25, end=time + 0.75)
    drums.notes.append(note)
for time in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25]:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.25)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Sax melody (D4, F#4, A4, B4)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5)
sax.notes.append(note)

# Marcus: Walking bass line (D2-G2, MIDI 38-43)
note = pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=41, start=1.75, end=2.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.5)
bass.notes.append(note)

# Diane: Open voicings, resolve on the last bar
# Bar 2: Dmaj7 (F#-A-C#-D)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)
piano.notes.append(note)

# Bar 3: Bm7 (D-F#-A-C#)
note = pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0)
piano.notes.append(note)

# Bar 4: G7 (B-D-F#-G)
note = pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=4.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0)
piano.notes.append(note)

# Drums in bars 2-4
for bar in range(2, 5):
    start_time = bar * bar_length
    for time in [0.0, 0.75]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start_time + time, end=start_time + time + 0.25)
        drums.notes.append(note)
    for time in [0.0, 0.75]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=start_time + time + 0.25, end=start_time + time + 0.75)
        drums.notes.append(note)
    for time in [0.0, 0.25, 0.5, 0.75, 1.0, 1.25]:
        note = pretty_midi.Note(velocity=80, pitch=42, start=start_time + time, end=start_time + time + 0.25)
        drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
