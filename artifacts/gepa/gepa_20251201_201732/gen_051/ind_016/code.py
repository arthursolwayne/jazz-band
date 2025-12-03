
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F minor (F, A, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0), # C2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, Fm7 -> G7 -> Am7 -> D7
piano_notes = [
    # Fm7: F, Ab, C, D
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75), # F2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75), # Ab2
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75), # C2
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75), # D2

    # G7: G, B, D, F
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5), # G2
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.5), # B2
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5), # D2
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5), # F2

    # Am7: A, C, E, G
    pretty_midi.Note(velocity=100, pitch=73, start=2.75, end=3.0), # A2
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0), # C2
    pretty_midi.Note(velocity=100, pitch=76, start=2.75, end=3.0), # E2
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0), # G2

    # D7: D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25), # D2
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25), # F#2
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.25), # A2
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25), # C2
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    bar_start = 1.5 + i * 1.5
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    for j in range(4):
        drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + j * 0.375, end=bar_start + j * 0.375 + 0.1875)
        drums.notes.append(drum_hihat)
    drums.notes.append(drum_kick)
    drums.notes.append(drum_snare)

# Sax: motif (F, Ab, D, Bb), start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.625), # F2
    pretty_midi.Note(velocity=110, pitch=72, start=1.625, end=1.75), # Ab2
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=1.875), # D2
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0), # Bb2
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F minor (F, A, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # D2
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5), # C2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, Fm7 -> G7 -> Am7 -> D7
piano_notes = [
    # Fm7: F, Ab, C, D
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25), # F2
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25), # C2
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25), # D2

    # G7: G, B, D, F
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0), # G2
    pretty_midi.Note(velocity=100, pitch=75, start=3.75, end=4.0), # B2
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0), # D2
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0), # F2

    # Am7: A, C, E, G
    pretty_midi.Note(velocity=100, pitch=73, start=4.25, end=4.5), # A2
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5), # C2
    pretty_midi.Note(velocity=100, pitch=76, start=4.25, end=4.5), # E2
    pretty_midi.Note(velocity=100, pitch=72, start=4.25, end=4.5), # G2

    # D7: D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75), # D2
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75), # F#2
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75), # A2
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75), # C2
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    bar_start = 3.0 + i * 1.5
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    for j in range(4):
        drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + j * 0.375, end=bar_start + j * 0.375 + 0.1875)
        drums.notes.append(drum_hihat)
    drums.notes.append(drum_kick)
    drums.notes.append(drum_snare)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F minor (F, A, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0), # C2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, Fm7 -> G7 -> Am7 -> D7
piano_notes = [
    # Fm7: F, Ab, C, D
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75), # F2
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75), # Ab2
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75), # C2
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75), # D2

    # G7: G, B, D, F
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5), # G2
    pretty_midi.Note(velocity=100, pitch=75, start=5.25, end=5.5), # B2
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5), # D2
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.5), # F2

    # Am7: A, C, E, G
    pretty_midi.Note(velocity=100, pitch=73, start=5.75, end=6.0), # A2
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0), # C2
    pretty_midi.Note(velocity=100, pitch=76, start=5.75, end=6.0), # E2
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0), # G2

    # D7: D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=74, start=6.0, end=6.25), # D2
    pretty_midi.Note(velocity=100, pitch=77, start=6.0, end=6.25), # F#2
    pretty_midi.Note(velocity=100, pitch=77, start=6.0, end=6.25), # A2
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.25), # C2
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    bar_start = 4.5 + i * 1.5
    drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    for j in range(4):
        drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + j * 0.375, end=bar_start + j * 0.375 + 0.1875)
        drums.notes.append(drum_hihat)
    drums.notes.append(drum_kick)
    drums.notes.append(drum_snare)

# Sax: complete the motif (F, Ab, D, Bb), resolve on the final beat
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.625), # F2
    pretty_midi.Note(velocity=110, pitch=72, start=4.625, end=4.75), # Ab2
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=4.875), # D2
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0), # Bb2
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
