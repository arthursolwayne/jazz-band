
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
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Sax: short motif, start it, leave it hanging, come back and finish
# Melody: Fm (F, Ab, Bb, D, Eb, G, Ab)
# Start with F, Ab, Bb, G (Fm7), then leave it hanging at G

for bar in range(2, 5):
    start = bar * 1.5
    # Sax: short motif (F, Ab, Bb, G)
    if bar == 2:
        sax_notes = [
            pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375),    # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 0.375, end=start + 0.75), # Ab
            pretty_midi.Note(velocity=100, pitch=67, start=start + 0.75, end=start + 1.125), # Bb
            pretty_midi.Note(velocity=100, pitch=76, start=start + 1.125, end=start + 1.5)  # G
        ]
    elif bar == 3:
        sax_notes = [
            pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375),    # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 0.375, end=start + 0.75), # Ab
            pretty_midi.Note(velocity=100, pitch=67, start=start + 0.75, end=start + 1.125), # Bb
            pretty_midi.Note(velocity=100, pitch=76, start=start + 1.125, end=start + 1.5)  # G
        ]
    elif bar == 4:
        sax_notes = [
            pretty_midi.Note(velocity=100, pitch=71, start=start, end=start + 0.375),    # F
            pretty_midi.Note(velocity=100, pitch=68, start=start + 0.375, end=start + 0.75), # Ab
            pretty_midi.Note(velocity=100, pitch=67, start=start + 0.75, end=start + 1.125), # Bb
            pretty_midi.Note(velocity=100, pitch=76, start=start + 1.125, end=start + 1.5)  # G
        ]
    sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
# Fm: F, Ab, Bb, D, Eb, G, Ab
# Walk: F, Gb, G, Ab, Bb, B, C, D, Eb, E, F, Gb, G, Ab, Bb, B, C, D
for bar in range(2, 5):
    start = bar * 1.5
    bass_notes = []
    for i in range(4):
        if bar == 2:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=71 + i, start=start + i * 0.375, end=start + i * 0.375 + 0.125))
        elif bar == 3:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=71 + i, start=start + i * 0.375, end=start + i * 0.375 + 0.125))
        elif bar == 4:
            bass_notes.append(pretty_midi.Note(velocity=80, pitch=71 + i, start=start + i * 0.375, end=start + i * 0.375 + 0.125))
    bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
for bar in range(2, 5):
    start = bar * 1.5
    if bar % 2 == 1:  # comp on 2 and 4
        piano_notes = [
            pretty_midi.Note(velocity=90, pitch=71, start=start, end=start + 0.375),
            pretty_midi.Note(velocity=90, pitch=68, start=start, end=start + 0.375),
            pretty_midi.Note(velocity=90, pitch=67, start=start, end=start + 0.375),
            pretty_midi.Note(velocity=90, pitch=64, start=start, end=start + 0.375)
        ]
    else:
        piano_notes = []
    piano.notes.extend(piano_notes)

# Drums: same pattern as bar 1
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
