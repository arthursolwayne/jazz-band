
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
drum_notes = []
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = []
bass_start_time = 1.5
bass_notes.append(pretty_midi.Note(velocity=90, pitch=45, start=bass_start_time, end=bass_start_time + 0.25))  # F
bass_notes.append(pretty_midi.Note(velocity=90, pitch=46, start=bass_start_time + 0.25, end=bass_start_time + 0.5))  # F#
bass_notes.append(pretty_midi.Note(velocity=90, pitch=44, start=bass_start_time + 0.5, end=bass_start_time + 0.75))  # E
bass_notes.append(pretty_midi.Note(velocity=90, pitch=45, start=bass_start_time + 0.75, end=bass_start_time + 1.0))  # F
bass_notes.append(pretty_midi.Note(velocity=90, pitch=47, start=bass_start_time + 1.0, end=bass_start_time + 1.25))  # G
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=bass_start_time + 1.25, end=bass_start_time + 1.5))  # A
bass_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=bass_start_time + 1.5, end=bass_start_time + 1.75))  # Ab
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=bass_start_time + 1.75, end=bass_start_time + 2.0))  # A
bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=bass_start_time + 2.0, end=bass_start_time + 2.25))  # Bb
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=bass_start_time + 2.25, end=bass_start_time + 2.5))  # A
bass_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=bass_start_time + 2.5, end=bass_start_time + 2.75))  # B
bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=bass_start_time + 2.75, end=bass_start_time + 3.0))  # Bb
bass_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=bass_start_time + 3.0, end=bass_start_time + 3.25))  # Ab
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=bass_start_time + 3.25, end=bass_start_time + 3.5))  # A
bass_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=bass_start_time + 3.5, end=bass_start_time + 3.75))  # B
bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=bass_start_time + 3.75, end=bass_start_time + 4.0))  # Bb
bass_notes.append(pretty_midi.Note(velocity=90, pitch=52, start=bass_start_time + 4.0, end=bass_start_time + 4.25))  # C
bass_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=bass_start_time + 4.25, end=bass_start_time + 4.5))  # B
bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=bass_start_time + 4.5, end=bass_start_time + 4.75))  # Bb
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=bass_start_time + 4.75, end=bass_start_time + 5.0))  # A
bass_notes.append(pretty_midi.Note(velocity=90, pitch=48, start=bass_start_time + 5.0, end=bass_start_time + 5.25))  # Ab
bass_notes.append(pretty_midi.Note(velocity=90, pitch=49, start=bass_start_time + 5.25, end=bass_start_time + 5.5))  # A
bass_notes.append(pretty_midi.Note(velocity=90, pitch=50, start=bass_start_time + 5.5, end=bass_start_time + 5.75))  # Bb
bass_notes.append(pretty_midi.Note(velocity=90, pitch=51, start=bass_start_time + 5.75, end=bass_start_time + 6.0))  # B

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = []
for bar in range(3):
    bar_start = 1.5 + bar * 1.5
    # Bar 2: 7th chord on F7 (F, A, C, Eb)
    if bar == 0:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_start, end=bar_start + 0.25))  # F
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=bar_start, end=bar_start + 0.25))  # A
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_start, end=bar_start + 0.25))  # C
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_start, end=bar_start + 0.25))  # Eb
    # Bar 3: 7th chord on Bb7 (Bb, D, F, Ab)
    elif bar == 1:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_start, end=bar_start + 0.25))  # Bb
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=73, start=bar_start, end=bar_start + 0.25))  # D
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=bar_start, end=bar_start + 0.25))  # F
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_start, end=bar_start + 0.25))  # Ab
    # Bar 4: 7th chord on Eb7 (Eb, G, Bb, Db)
    elif bar == 2:
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=68, start=bar_start, end=bar_start + 0.25))  # Eb
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=bar_start, end=bar_start + 0.25))  # G
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=70, start=bar_start, end=bar_start + 0.25))  # Bb
        piano_notes.append(pretty_midi.Note(velocity=90, pitch=67, start=bar_start, end=bar_start + 0.25))  # Db

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []
sax_start_time = 1.5
# Motif: F, G, Bb, F (half note, quarter note, eighth note, eighth note)
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=sax_start_time, end=sax_start_time + 0.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=73, start=sax_start_time + 0.5, end=sax_start_time + 0.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=70, start=sax_start_time + 0.75, end=sax_start_time + 0.875))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=71, start=sax_start_time + 0.875, end=sax_start_time + 1.0))

# Repeat the motif an octave higher
sax_notes.append(pretty_midi.Note(velocity=110, pitch=83, start=sax_start_time + 2.0, end=sax_start_time + 2.5))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=85, start=sax_start_time + 2.5, end=sax_start_time + 2.75))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=82, start=sax_start_time + 2.75, end=sax_start_time + 2.875))
sax_notes.append(pretty_midi.Note(velocity=110, pitch=83, start=sax_start_time + 2.875, end=sax_start_time + 3.0))

sax.notes.extend(sax_notes)

# Drums: Continue the same pattern for bars 2-4
for bar in range(2, 4):
    bar_start = 1.5 + bar * 1.5
    for beat in range(4):
        time = bar_start + beat * 0.375
        if beat == 0 or beat == 2:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
