
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
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm (F2, Ab2, Bb2, Db2, etc.) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # Gb2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # F2
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=36, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=80, pitch=34, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=80, pitch=34, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # Gb2
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875), # Ab4
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875), # Eb4

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F5
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Ab4

    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375), # Eb4
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375), # Db4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on beat 2 and 4
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4])

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm melody: F, Ab, Bb, Eb (start on F, leave on Ab, return on Bb, resolve on Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875), # F4
    pretty_midi.Note(velocity=100, pitch=51, start=1.6875, end=1.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.4375), # Bb4
    pretty_midi.Note(velocity=100, pitch=50, start=2.4375, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.1875), # Eb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
