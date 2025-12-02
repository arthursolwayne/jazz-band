
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
for bar in range(1):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    hihat0 = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375)
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.375, end=time + 0.75)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.75, end=time + 1.125)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat0, hihat1, hihat2, hihat3])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62, 100, 0.375), # D
    (1.875, 61, 100, 0.375), # C#
    (2.25, 64, 100, 0.375), # E
    (2.625, 65, 100, 0.375), # F
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62, 100, 0.375), # D
    (3.375, 63, 100, 0.375), # D#
    (3.75, 67, 100, 0.375), # G
    (4.125, 65, 100, 0.375), # F
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62, 100, 0.375), # D
    (4.875, 61, 100, 0.375), # C#
    (5.25, 64, 100, 0.375), # E
    (5.625, 65, 100, 0.375), # F
]
for note in bass_notes:
    start, pitch, velocity, duration = note
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bar 2: D7 (D, F#, A, C)
chord_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62, 100, 0.375), # D
    (1.5, 67, 100, 0.375), # A
    (1.5, 64, 100, 0.375), # F#
    (1.5, 60, 100, 0.375), # C
    # Bar 3 (3.0 - 4.5s)
    (3.0, 62, 100, 0.375), # D
    (3.0, 67, 100, 0.375), # A
    (3.0, 64, 100, 0.375), # F#
    (3.0, 60, 100, 0.375), # C
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62, 100, 0.375), # D
    (4.5, 67, 100, 0.375), # A
    (4.5, 64, 100, 0.375), # F#
    (4.5, 60, 100, 0.375), # C
]
for note in chord_notes:
    start, pitch, velocity, duration = note
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + duration))

# Sax: One short motif, make it sing
# Bar 2, 1st 8th note: D (62)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875))
# Bar 2, 2nd 8th note: F# (67)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25))
# Bar 3, 1st 8th note: D (62)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375))
# Bar 3, 2nd 8th note: C (60)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.75))
# Bar 4, 3rd 8th note: F# (67)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625))
# Bar 4, 4th 8th note: D (62)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0))

# Drums: Bar 2-4
for bar in range(2, 5):
    time = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=time + 0.375, end=time + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=time + 1.125, end=time + 1.5)
    # Hihat on every eighth
    hihat0 = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375)
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.375, end=time + 0.75)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=time + 0.75, end=time + 1.125)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=time + 1.125, end=time + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat0, hihat1, hihat2, hihat3])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
