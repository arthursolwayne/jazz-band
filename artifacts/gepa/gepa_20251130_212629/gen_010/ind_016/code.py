
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
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
# In D minor, bass line: D, Eb, F, G, A, Bb, C, D
bass_notes = [62, 63, 65, 67, 69, 70, 72, 62]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
# Bm7b5 = B, D, F, A
# G7 = G, B, D, F
# Cm7 = C, Eb, G, Bb
piano_notes = [
    # Bar 2 (beat 1) D7: D, F#, A, C
    (62, 1.5), (67, 1.5), (69, 1.5), (60, 1.5),
    # Bar 2 (beat 2) Bm7b5: B, D, F, A
    (67, 1.875), (62, 1.875), (65, 1.875), (69, 1.875),
    # Bar 3 (beat 3) G7: G, B, D, F
    (67, 2.625), (69, 2.625), (62, 2.625), (65, 2.625),
    # Bar 3 (beat 4) Cm7: C, Eb, G, Bb
    (60, 3.0), (63, 3.0), (67, 3.0), (61, 3.0),
    # Bar 4 (beat 1) D7: D, F#, A, C
    (62, 3.375), (67, 3.375), (69, 3.375), (60, 3.375),
    # Bar 4 (beat 2) Bm7b5: B, D, F, A
    (67, 3.75), (62, 3.75), (65, 3.75), (69, 3.75),
    # Bar 4 (beat 3) G7: G, B, D, F
    (67, 4.5), (69, 4.5), (62, 4.5), (65, 4.5),
    # Bar 4 (beat 4) Cm7: C, Eb, G, Bb
    (60, 4.875), (63, 4.875), (67, 4.875), (61, 4.875),
]
for pitch, start in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Drums: same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: short motif, start it, leave it hanging, finish it
# D, F#, A, C, D (D minor scale)
sax_notes = [
    (62, 1.5), (67, 1.5), (69, 1.5), (60, 1.5),  # Bar 2, beat 1
    (62, 2.125), (67, 2.125), (69, 2.125), (60, 2.125),  # Bar 2, beat 2
    (62, 2.5), (67, 2.5), (69, 2.5), (60, 2.5),  # Bar 2, beat 3
    (62, 3.0), (67, 3.0), (69, 3.0), (60, 3.0),  # Bar 3, beat 1
    (62, 3.5), (67, 3.5), (69, 3.5), (60, 3.5),  # Bar 3, beat 2
    (62, 4.0), (67, 4.0), (69, 4.0), (60, 4.0),  # Bar 3, beat 3
    (62, 4.5), (67, 4.5), (69, 4.5), (60, 4.5),  # Bar 4, beat 1
    (62, 5.0), (67, 5.0), (69, 5.0), (60, 5.0)   # Bar 4, beat 2
]
for pitch, start in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

# Save the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
