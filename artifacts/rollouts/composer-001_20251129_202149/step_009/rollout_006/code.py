
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1& (eighth note)
    (42, 0.375, 0.1875), # Hihat on 2&
    (42, 0.75, 0.1875), # Hihat on 3&
    (42, 1.125, 0.1875), # Hihat on 4&
    (36, 1.5, 0.375),  # Kick on 3
    (38, 2.25, 0.375), # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Drums continue
for i in range(2, 6):
    start = i * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = [pretty_midi.Note(velocity=100, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.1875) for j in range(4)]
    drums.notes.extend([kick, snare] + hihat)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375), # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375), # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375), # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375), # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375), # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375), # A#
    (71, 5.625, 0.375), # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (60, 1.5, 0.375), # C
    (64, 1.5, 0.375), # E
    (67, 1.5, 0.375), # G
    (71, 1.5, 0.375), # B
    (64, 2.25, 0.375), # E
    (67, 2.25, 0.375), # G
    (71, 2.25, 0.375), # B
    (74, 2.25, 0.375), # D
    # Bar 3 (3.0 - 4.5s)
    (60, 3.0, 0.375), # C
    (64, 3.0, 0.375), # E
    (67, 3.0, 0.375), # G
    (71, 3.0, 0.375), # B
    (64, 3.75, 0.375), # E
    (67, 3.75, 0.375), # G
    (71, 3.75, 0.375), # B
    (74, 3.75, 0.375), # D
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 0.375), # C
    (64, 4.5, 0.375), # E
    (67, 4.5, 0.375), # G
    (71, 4.5, 0.375), # B
    (64, 5.25, 0.375), # E
    (67, 5.25, 0.375), # G
    (71, 5.25, 0.375), # B
    (74, 5.25, 0.375), # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - E - G - B (Cmaj7) but played as quarter notes with space between
sax_notes = [
    (60, 1.5, 0.375), # C
    (64, 2.25, 0.375), # E
    (67, 3.0, 0.375), # G
    (71, 3.75, 0.375), # B
    (60, 4.5, 0.375), # C
    (64, 5.25, 0.375), # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
