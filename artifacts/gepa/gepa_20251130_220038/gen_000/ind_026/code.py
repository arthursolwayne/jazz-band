
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
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on beat 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: motif starting on F (70), then Bb (71), D (69), G (71), F (70) - hang on the last note
for bar in range(2, 5):
    start = bar * 1.5
    # Sax phrase
    sax_notes = [
        pretty_midi.Note(velocity=110, pitch=70, start=start, end=start + 0.375),
        pretty_midi.Note(velocity=110, pitch=71, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=110, pitch=69, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=110, pitch=71, start=start + 1.125, end=start + 1.5)
    ]
    sax.notes.extend(sax_notes)

    # Bass: walking line in F minor (F, Gb, G, A)
    # Each note on 1, 2, 3, 4
    if bar == 2:
        bass_notes = [
            pretty_midi.Note(velocity=90, pitch=70, start=start, end=start + 0.375),
            pretty_midi.Note(velocity=90, pitch=68, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=90, pitch=69, start=start + 0.75, end=start + 1.125),
            pretty_midi.Note(velocity=90, pitch=71, start=start + 1.125, end=start + 1.5)
        ]
    elif bar == 3:
        bass_notes = [
            pretty_midi.Note(velocity=90, pitch=68, start=start, end=start + 0.375),
            pretty_midi.Note(velocity=90, pitch=69, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=90, pitch=71, start=start + 0.75, end=start + 1.125),
            pretty_midi.Note(velocity=90, pitch=70, start=start + 1.125, end=start + 1.5)
        ]
    else:  # bar == 4
        bass_notes = [
            pretty_midi.Note(velocity=90, pitch=69, start=start, end=start + 0.375),
            pretty_midi.Note(velocity=90, pitch=71, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=90, pitch=70, start=start + 0.75, end=start + 1.125),
            pretty_midi.Note(velocity=90, pitch=68, start=start + 1.125, end=start + 1.5)
        ]
    bass.notes.extend(bass_notes)

    # Piano: 7th chords on 2 and 4
    # F7 on 2, Bb7 on 4
    if bar == 2:
        # F7 (F, A, C, Eb)
        piano_notes = [
            pretty_midi.Note(velocity=95, pitch=70, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=72, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=74, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=68, start=start + 0.375, end=start + 0.75)
        ]
    elif bar == 3:
        # Bb7 (Bb, D, F, Ab)
        piano_notes = [
            pretty_midi.Note(velocity=95, pitch=68, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=71, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=70, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=65, start=start + 0.375, end=start + 0.75)
        ]
    else:  # bar == 4
        # F7 on 2, Bb7 on 4
        piano_notes = [
            pretty_midi.Note(velocity=95, pitch=70, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=72, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=74, start=start + 0.375, end=start + 0.75),
            pretty_midi.Note(velocity=95, pitch=68, start=start + 0.375, end=start + 0.75)
        ]
    piano.notes.extend(piano_notes)

    # Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
