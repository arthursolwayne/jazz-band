
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    (36, 0.0, 1.0),          # Kick on beat 1
    (38, 0.5, 1.0),          # Snare on beat 2
    (42, 0.0, 1.0),          # Hihat on beat 1
    (42, 0.25, 0.25),        # Hihat on 1 &
    (42, 0.5, 0.25),         # Hihat on 2 &
    (42, 0.75, 0.25),        # Hihat on 3 &
    (42, 1.0, 0.25),         # Hihat on 4 &
    (36, 1.5, 1.0),          # Kick on beat 3
    (38, 1.5, 1.0),          # Snare on beat 4
    (42, 1.5, 0.25),         # Hihat on 3
    (42, 1.75, 0.25),        # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D
bass_notes = [
    (62, 1.5, 0.375),       # D4 (beat 1)
    (64, 1.875, 0.375),     # F#4 (beat 2)
    (65, 2.25, 0.375),      # G4 (beat 3)
    (62, 2.625, 0.375),     # D4 (beat 4)
    (67, 2.625, 0.375),     # A4 (beat 1)
    (64, 3.0, 0.375),       # F#4 (beat 2)
    (62, 3.375, 0.375),     # D4 (beat 3)
    (67, 3.75, 0.375),      # A4 (beat 4)
    (69, 3.75, 0.375),      # B4 (beat 1)
    (67, 4.125, 0.375),     # A4 (beat 2)
    (69, 4.5, 0.375),       # B4 (beat 3)
    (67, 4.875, 0.375),     # A4 (beat 4)
    (65, 4.875, 0.375),     # G4 (beat 1)
    (62, 5.25, 0.375),      # D4 (beat 2)
    (64, 5.625, 0.375),     # F#4 (beat 3)
    (62, 6.0, 0.375),       # D4 (beat 4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (67, 2.0, 0.375),   # A4 (beat 2)
    (69, 2.0, 0.375),   # B4
    (71, 2.0, 0.375),   # C#5
    (62, 2.0, 0.375),   # D4
    (67, 4.0, 0.375),   # A4 (beat 4)
    (69, 4.0, 0.375),   # B4
    (71, 4.0, 0.375),   # C#5
    (62, 4.0, 0.375),   # D4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 1.0),          # Kick on beat 1
    (38, 2.0, 1.0),          # Snare on beat 2
    (42, 1.5, 0.25),         # Hihat on 1
    (42, 1.75, 0.25),        # Hihat on 1 &
    (42, 2.0, 0.25),         # Hihat on 2
    (42, 2.25, 0.25),        # Hihat on 2 &
    (42, 2.5, 0.25),         # Hihat on 3
    (42, 2.75, 0.25),        # Hihat on 3 &
    (42, 3.0, 0.25),         # Hihat on 4
    (42, 3.25, 0.25),        # Hihat on 4 &
    (36, 3.0, 1.0),          # Kick on beat 3
    (38, 3.5, 1.0),          # Snare on beat 4
    (42, 3.0, 0.25),         # Hihat on 3
    (42, 3.25, 0.25),        # Hihat on 4
    (36, 4.5, 1.0),          # Kick on beat 1
    (38, 5.0, 1.0),          # Snare on beat 2
    (42, 4.5, 0.25),         # Hihat on 1
    (42, 4.75, 0.25),        # Hihat on 1 &
    (42, 5.0, 0.25),         # Hihat on 2
    (42, 5.25, 0.25),        # Hihat on 2 &
    (42, 5.5, 0.25),         # Hihat on 3
    (42, 5.75, 0.25),        # Hihat on 3 &
    (42, 6.0, 0.25),         # Hihat on 4
    (36, 5.5, 1.0),          # Kick on beat 3
    (38, 6.0, 1.0),          # Snare on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: 4-bar motif in D
# Tenor sax melody: D, F#, B, C#, A (quarter notes)
sax_notes = [
    (62, 1.5, 0.375),   # D4 (beat 1)
    (67, 1.875, 0.375), # A4 (beat 2)
    (69, 2.25, 0.375),  # B4 (beat 3)
    (71, 2.625, 0.375), # C#5 (beat 4)
    (67, 3.0, 0.375),   # A4 (beat 1)
    (69, 3.375, 0.375), # B4 (beat 2)
    (65, 3.75, 0.375),  # G4 (beat 3)
    (62, 4.125, 0.375), # D4 (beat 4)
    (67, 4.5, 0.375),   # A4 (beat 1)
    (69, 4.875, 0.375), # B4 (beat 2)
    (67, 5.25, 0.375),  # A4 (beat 3)
    (62, 5.625, 0.375), # D4 (beat 4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_shorter_intro.mid')
