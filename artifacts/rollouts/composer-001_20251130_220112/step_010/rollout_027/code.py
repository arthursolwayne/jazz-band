
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
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5, note_number=42)
    drums.notes.extend([kick, snare, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches, never the same note twice
# Fm: F, Ab, C, D, Eb, G, Bb, Db
bass_notes = [77, 79, 81, 82, 83, 85, 87, 89]  # F, Ab, C, D, Eb, G, Bb, Db
bass_pattern = [77, 79, 81, 82, 83, 85, 87, 89, 85, 83, 82, 81, 79, 77, 81, 82]
for i, note in enumerate(bass_pattern):
    start = 1.5 + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bbm7 = Bb, Db, F, Ab
for bar in range(2, 5):
    start = bar * 1.5
    if bar % 2 == 0:
        # Fm7 on beat 2
        f7 = pretty_midi.Note(velocity=90, pitch=77, start=start + 0.75, end=start + 1.125)
        ab7 = pretty_midi.Note(velocity=90, pitch=79, start=start + 0.75, end=start + 1.125)
        c7 = pretty_midi.Note(velocity=90, pitch=81, start=start + 0.75, end=start + 1.125)
        eb7 = pretty_midi.Note(velocity=90, pitch=83, start=start + 0.75, end=start + 1.125)
        piano.notes.extend([f7, ab7, c7, eb7])
    else:
        # Bbm7 on beat 4
        bb7 = pretty_midi.Note(velocity=90, pitch=87, start=start + 1.125, end=start + 1.5)
        db7 = pretty_midi.Note(velocity=90, pitch=89, start=start + 1.125, end=start + 1.5)
        f7 = pretty_midi.Note(velocity=90, pitch=77, start=start + 1.125, end=start + 1.5)
        ab7 = pretty_midi.Note(velocity=90, pitch=79, start=start + 1.125, end=start + 1.5)
        piano.notes.extend([bb7, db7, f7, ab7])

# Drums: same pattern as bar 1, repeated for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5, note_number=42)
    drums.notes.extend([kick, snare, hihat])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (77), Ab (79), Eb (83), F (77) — short and suspended
# Play on beat 2 of bar 2
sax_note1 = pretty_midi.Note(velocity=110, pitch=77, start=1.5 + 0.75, end=1.5 + 1.125)
sax_note2 = pretty_midi.Note(velocity=110, pitch=79, start=1.5 + 0.75, end=1.5 + 1.125)
sax_note3 = pretty_midi.Note(velocity=110, pitch=83, start=1.5 + 0.75, end=1.5 + 1.125)
sax_note4 = pretty_midi.Note(velocity=110, pitch=77, start=1.5 + 1.5, end=1.5 + 1.875)
sax.notes.extend([sax_note1, sax_note2, sax_note3, sax_note4])

midi.instruments.extend([sax, bass, piano, drums])
