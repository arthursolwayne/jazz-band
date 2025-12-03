
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.375, 42, 80), # Hihat on 1&
    (0.75, 38, 100), # Snare on beat 2
    (0.75, 42, 80), # Hihat on 2&
    (1.125, 42, 80), # Hihat on 3&
    (1.5, 36, 100),  # Kick on beat 3
    (1.875, 42, 80), # Hihat on 3&
    (2.25, 38, 100), # Snare on beat 4
    (2.25, 42, 80),  # Hihat on 4&
    (2.625, 42, 80), # Hihat on 4&
]

for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(
        velocity=velocity,
        pitch=note,
        start=time,
        end=time + 0.125
    ))

# Bar 2: Sax enters with a motif, piano and bass join

# Bass line: Walking line in Fm, roots and fifths with chromatic approaches
# Fm = F, Ab, D, C
bass_notes = [
    (1.5, 38, 80), # F2 (MIDI 38)
    (1.875, 41, 70), # Eb2 (chromatic approach)
    (2.25, 37, 80), # D2 (MIDI 37)
    (2.625, 35, 70), # C2 (chromatic approach)
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(
        velocity=velocity,
        pitch=note,
        start=time,
        end=time + 0.375
    ))

# Piano chords: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Ab7 (Ab, C, Eb, G)
piano_notes = [
    # Bar 2: Fm7
    (1.5, 64, 100), # F4 (MIDI 64)
    (1.5, 69, 80), # Ab4 (MIDI 69)
    (1.5, 72, 100), # C5 (MIDI 72)
    (1.5, 71, 80), # D5 (MIDI 71)
    # Bar 3: Bb7
    (2.25, 62, 100), # Bb4 (MIDI 62)
    (2.25, 67, 80), # D5 (MIDI 67)
    (2.25, 64, 100), # F5 (MIDI 64)
    (2.25, 69, 80), # Ab5 (MIDI 69)
    # Bar 4: Ab7
    (3.0, 65, 100), # Ab4 (MIDI 65)
    (3.0, 68, 80), # C5 (MIDI 68)
    (3.0, 71, 100), # Eb5 (MIDI 71)
    (3.0, 76, 80), # G5 (MIDI 76)
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(
        velocity=velocity,
        pitch=note,
        start=time,
        end=time + 0.375
    ))

# Sax melody: One short motif, haunting and incomplete
# Start it, leave it hanging, come back to finish it
sax_notes = [
    (1.5, 62, 100), # F4 (MIDI 62)
    (1.75, 65, 90), # Ab4 (MIDI 65)
    (2.0, 62, 100), # F4
    (2.25, 67, 90), # Bb4 (MIDI 67)
    (2.5, 62, 100), # F4
    (2.75, 65, 90), # Ab4
    (3.0, 62, 100), # F4
    (3.25, 67, 90), # Bb4
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(
        velocity=velocity,
        pitch=note,
        start=time,
        end=time + 0.25
    ))

# Bar 3: Drums continue with the same pattern
for i in range(1, 4):
    for time, note, velocity in drum_notes:
        drums.notes.append(pretty_midi.Note(
            velocity=velocity,
            pitch=note,
            start=time + (i * 1.5),
            end=time + (i * 1.5) + 0.125
        ))

# Bar 4: Drums continue with same pattern
# No additional notes needed, already handled

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
