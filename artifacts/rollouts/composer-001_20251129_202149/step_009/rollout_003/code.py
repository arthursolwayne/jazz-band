
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 1.0),   # Kick on 1
    (38, 0.5, 1.0),   # Snare on 2
    (42, 0.0, 1.0),   # Hihat on 1
    (42, 0.5, 1.0),   # Hihat on 2
    (42, 1.0, 1.0),   # Hihat on 3
    (42, 1.5, 1.0),   # Hihat on 4
    (36, 1.5, 1.0)    # Kick on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
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
    (72, 6.0, 0.375) # C
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.5, 0.375), # C7 (C, E, B)
    (64, 1.5, 0.375),
    (67, 1.5, 0.375),
    (69, 1.5, 0.375),
    # Bar 3
    (60, 3.0, 0.375),
    (64, 3.0, 0.375),
    (67, 3.0, 0.375),
    (69, 3.0, 0.375),
    # Bar 4
    (60, 4.5, 0.375),
    (64, 4.5, 0.375),
    (67, 4.5, 0.375),
    (69, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drum_note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(drum_note)
    # Snare on 2
    drum_note = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.5, end=start + 0.5 + 0.375)
    drums.notes.append(drum_note)
    # Kick on 3
    drum_note = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375)
    drums.notes.append(drum_note)
    # Snare on 4
    drum_note = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.0, end=start + 1.0 + 0.375)
    drums.notes.append(drum_note)
    # Hihat on every eighth
    for i in range(4):
        drum_note = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        drums.notes.append(drum_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C, E, B, D (C7 arpeggio), then leave it hanging on B
sax_notes = [
    (60, 1.5, 0.375), # C
    (64, 1.875, 0.375), # E
    (67, 2.25, 0.375), # B
    (62, 2.625, 0.375), # D
    (67, 3.0, 0.375), # B
    (67, 3.375, 0.375), # B
    (67, 3.75, 0.375), # B
    (67, 4.125, 0.375), # B
    (67, 4.5, 0.375), # B
    (67, 4.875, 0.375), # B
    (67, 5.25, 0.375), # B
    (67, 5.625, 0.375), # B
    (67, 6.0, 0.375) # B
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(tempo=120, time=0.0)]

midi.write("wayne_intro.mid")
