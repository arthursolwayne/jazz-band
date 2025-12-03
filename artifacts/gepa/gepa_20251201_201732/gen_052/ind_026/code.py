
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 1.5, 1.625), # D2
    (40, 1.625, 1.75), # E2
    (43, 1.75, 1.875), # G2
    (41, 1.875, 2.0), # F#2
    (38, 2.0, 2.125), # D2
    (40, 2.125, 2.25), # E2
    (43, 2.25, 2.375), # G2
    (41, 2.375, 2.5), # F#2
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0)) # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0)) # F#4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0)) # A4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0)) # C#5

# Bar 3: G7 (G B D F#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5)) # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5)) # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5)) # F#4

# Bar 4: C7 (C E G B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0)) # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0)) # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0)) # B4

# Bar 2: Dante on sax - motif
sax_notes = [
    (65, 1.5, 1.75), # E4
    (67, 1.75, 2.0), # G4
    (69, 2.0, 2.125), # A4
    (67, 2.125, 2.25), # G4
    (65, 2.25, 2.375), # E4
    (62, 2.375, 2.5), # D4
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: walking line (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 3.0, 3.125), # D2
    (40, 3.125, 3.25), # E2
    (43, 3.25, 3.375), # G2
    (41, 3.375, 3.5), # F#2
    (38, 3.5, 3.625), # D2
    (40, 3.625, 3.75), # E2
    (43, 3.75, 3.875), # G2
    (41, 3.875, 4.0), # F#2
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G B D F#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5)) # B4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5)) # D4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5)) # F#4

# Bar 4: C7 (C E G B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0)) # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0)) # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0)) # B4

# Bar 3: Dante on sax - continuation
sax_notes = [
    (62, 3.0, 3.125), # D4
    (64, 3.125, 3.25), # E4
    (67, 3.25, 3.375), # G4
    (65, 3.375, 3.5), # F#4
    (62, 3.5, 3.625), # D4
    (64, 3.625, 3.75), # E4
    (67, 3.75, 3.875), # G4
    (65, 3.875, 4.0), # F#4
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 4: Full quartet (4.0 - 5.5s)

# Marcus on bass: walking line (D2-G2, MIDI 38-43)
bass_notes = [
    (38, 4.0, 4.125), # D2
    (40, 4.125, 4.25), # E2
    (43, 4.25, 4.375), # G2
    (41, 4.375, 4.5), # F#2
    (38, 4.5, 4.625), # D2
    (40, 4.625, 4.75), # E2
    (43, 4.75, 4.875), # G2
    (41, 4.875, 5.0), # F#2
]
for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C E G B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.5)) # C4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.5)) # E4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.5)) # G4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.5)) # B4

# Bar 4: Dante on sax - final resolution
sax_notes = [
    (60, 4.0, 4.125), # C4
    (62, 4.125, 4.25), # D4
    (64, 4.25, 4.375), # E4
    (67, 4.375, 4.5), # G4
    (65, 4.5, 4.625), # F#4
    (62, 4.625, 4.75), # D4
    (60, 4.75, 5.0), # C4
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Bar 4: Drums
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.125, end=5.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0))

# Hihat on every eighth
for i in range(4):
    start = 4.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
