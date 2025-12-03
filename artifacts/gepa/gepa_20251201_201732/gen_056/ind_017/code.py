
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
drum_notes = [
    (0.0, 36, 100), (0.375, 42, 100),
    (0.75, 38, 100), (1.125, 42, 100),
    (1.5, 36, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100)
]
for time, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)

# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38, 100), (1.875, 40, 100), (2.25, 43, 100), (2.625, 38, 100),
    (3.0, 40, 100), (3.375, 43, 100), (3.75, 42, 100), (4.125, 38, 100)
]
for time, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 - G7 - Cm7 - F7
# Dm7 (D F A C) = 38, 41, 45, 48
# G7 (G B D F) = 43, 47, 49, 51
# Cm7 (C Eb G Bb) = 40, 43, 47, 49
# F7 (F A C Eb) = 45, 48, 50, 53
piano_notes = [
    (1.5, 48, 100), (1.5, 45, 100), (1.5, 41, 100), (1.5, 38, 100),
    (2.25, 51, 100), (2.25, 49, 100), (2.25, 47, 100), (2.25, 43, 100),
    (3.0, 49, 100), (3.0, 47, 100), (3.0, 43, 100), (3.0, 40, 100),
    (3.75, 53, 100), (3.75, 50, 100), (3.75, 48, 100), (3.75, 45, 100)
]
for time, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Tenor sax, short motif, make it sing
# Start on D, then Bb, then F, each on off-beats
sax_notes = [
    (1.5, 50, 100), (1.875, 46, 80), (2.25, 52, 100), (2.625, 46, 80),
    (3.0, 50, 100), (3.375, 46, 80), (3.75, 52, 100), (4.125, 46, 80)
]
for time, note, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)

# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 40, 100), (3.375, 43, 100), (3.75, 38, 100), (4.125, 40, 100),
    (4.5, 43, 100), (4.875, 42, 100), (5.25, 38, 100), (5.625, 40, 100)
]
for time, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 - G7 - Cm7 - F7
piano_notes = [
    (3.0, 48, 100), (3.0, 45, 100), (3.0, 41, 100), (3.0, 38, 100),
    (3.75, 51, 100), (3.75, 49, 100), (3.75, 47, 100), (3.75, 43, 100),
    (4.5, 49, 100), (4.5, 47, 100), (4.5, 43, 100), (4.5, 40, 100),
    (5.25, 53, 100), (5.25, 50, 100), (5.25, 48, 100), (5.25, 45, 100)
]
for time, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Tenor sax, continuation of motif, slightly varied
sax_notes = [
    (3.0, 50, 100), (3.375, 46, 80), (3.75, 52, 100), (4.125, 46, 80),
    (4.5, 50, 100), (4.875, 46, 80), (5.25, 52, 100), (5.625, 46, 80)
]
for time, note, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)

# Marcus: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 40, 100), (4.875, 43, 100), (5.25, 38, 100), (5.625, 40, 100)
]
for time, note, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 - G7 - Cm7 - F7
piano_notes = [
    (4.5, 48, 100), (4.5, 45, 100), (4.5, 41, 100), (4.5, 38, 100),
    (5.25, 51, 100), (5.25, 49, 100), (5.25, 47, 100), (5.25, 43, 100),
    (6.0, 49, 100), (6.0, 47, 100), (6.0, 43, 100), (6.0, 40, 100)
]
for time, note, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Tenor sax, finish the motif with a resolution
sax_notes = [
    (4.5, 50, 100), (4.875, 46, 80), (5.25, 52, 100), (5.625, 46, 80),
    (6.0, 50, 100), (6.0, 46, 80)
]
for time, note, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note)

# Drums: Bar 3-4 (3.0 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100), (3.375, 42, 100),
    (3.75, 38, 100), (4.125, 42, 100),
    (4.5, 36, 100), (4.875, 42, 100),
    (5.25, 38, 100), (5.625, 42, 100)
]
for time, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
