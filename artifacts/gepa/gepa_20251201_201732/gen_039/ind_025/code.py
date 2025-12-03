
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
for tick in range(0, 120, 12):  # 12 ticks per beat at 160 BPM (60 * 160 / 120 = 80 ticks per beat)
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=tick, end=tick + 6))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=tick + 6, end=tick + 12))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=tick, end=tick + 12))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, roots and fifths with chromatic approaches
# D2 (D), F#2 (F#), A2 (A), C#3 (C#), D3 (D), F#3 (F#), A3 (A), C#4 (C#)
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=38, start=120, end=126)),  # D2
    (pretty_midi.Note(velocity=100, pitch=41, start=126, end=132)),  # F#2
    (pretty_midi.Note(velocity=100, pitch=45, start=132, end=138)),  # A2
    (pretty_midi.Note(velocity=100, pitch=47, start=138, end=144)),  # C#3
    (pretty_midi.Note(velocity=100, pitch=48, start=144, end=150)),  # D3
    (pretty_midi.Note(velocity=100, pitch=51, start=150, end=156)),  # F#3
    (pretty_midi.Note(velocity=100, pitch=55, start=156, end=162)),  # A3
    (pretty_midi.Note(velocity=100, pitch=57, start=162, end=168)),  # C#4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=120, end=144))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=120, end=144))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=120, end=144))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=120, end=144))  # C#

# Bar 3: G7 (G, B, D, F#)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=144, end=168))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=144, end=168))  # B
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=144, end=168))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=144, end=168))  # F#

# Bar 4: C7 (C, E, G, B)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=168, end=192))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=168, end=192))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=168, end=192))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=86, start=168, end=192))  # B

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (E) -> G (Bb) -> A (B) -> D (C#), then repeat with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=120, end=126),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=126, end=132),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=132, end=138),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=138, end=144),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=144, end=150),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=150, end=156),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=156, end=162),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=162, end=168),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=168, end=174),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=174, end=180),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=180, end=186),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=186, end=192),  # B
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 120 * bar
    for tick in range(0, 120, 12):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + tick, end=bar_start + tick + 6))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + tick + 6, end=bar_start + tick + 12))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + tick, end=bar_start + tick + 12))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
